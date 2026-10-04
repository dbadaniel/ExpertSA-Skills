# Gera stubs PHP (constantes e classes mínimas) a partir do código real do Elementor.
import re, glob, os
E = os.environ['ELEMENTOR_SRC'].rstrip('/') + '/'; W = os.environ['WORK']
HERE = os.path.dirname(os.path.abspath(__file__))
def consts(path):
    return re.findall(r"^\s*const\s+([A-Z0-9_]+)\s*=\s*('[^']*')\s*;", open(E+path).read(), re.M)
def cblock(cls, cs): return "class %s { %s }\n" % (cls, "".join("const %s = %s; " % c for c in cs))
groups = {}
for f in glob.glob(E+'includes/controls/groups/*.php'):
    s = open(f).read(); m = re.search(r"class (Group_Control_\w+)", s)
    t = re.search(r"public static function get_type\(\)\s*\{\s*return\s*'([^']+)'", s)
    if m and t: groups[m.group(1)] = t.group(1)
base = open(os.path.join(HERE, 'base.php.inc')).read()
head = ["<?php\n",
 "namespace Elementor\\Core\\Kits\\Documents\\Tabs { ", cblock('Global_Colors', consts('core/kits/documents/tabs/global-colors.php')),
 cblock('Global_Typography', [c for c in consts('core/kits/documents/tabs/global-typography.php') if not c[0].endswith('PREFIX')]), "}\n",
 "namespace Elementor\\Core\\Breakpoints { " + cblock('Manager', consts('core/breakpoints/manager.php')) + "}\n",
 "namespace Elementor\\Core\\Settings\\Page { class Manager { const META_KEY='_elementor_page_settings'; public static function __callStatic($n,$a){return '';} } }\n",
 "namespace Elementor\\Core\\Utils { class Hints { public static function __callStatic($n,$a){return '';} } }\n",
 "namespace Elementor\\Modules\\ContentSanitizer\\Interfaces { interface Sanitizable { } }\n",
 "namespace Elementor\\Modules\\DynamicTags { class Module { const TEXT_CATEGORY='text'; const URL_CATEGORY='url'; const POST_META_CATEGORY='post_meta'; const NUMBER_CATEGORY='number'; const IMAGE_CATEGORY='image'; const MEDIA_CATEGORY='media'; const GALLERY_CATEGORY='gallery'; const COLOR_CATEGORY='color'; const DATETIME_CATEGORY='datetime'; const BASE_GROUP='base'; } }\n",
 "namespace Elementor\\Modules\\Promotions\\Controls { class Promotion_Control { const TYPE='promotion_control'; public static function get_type(){return 'promotion_control';} } }\n",
 "namespace Elementor\\Core\\Admin { class Admin_Notices { public static function __callStatic($n,$a){return '';} } }\n",
 "namespace Elementor {\n" + cblock('Controls_Manager', consts('includes/managers/controls.php')) + base]
gstubs = "".join("class %s { public static function get_type(){return '%s';} public static function __callStatic($n,$a){return '';} }\n" % kv for kv in groups.items())
open(W+'/stubs_gen.php', 'w').write("".join(head) + gstubs + "}\n")
extra = ("abstract class Group_Control_Base { use Capture; public function __construct(){} public static function __callStatic($n,$a){return [];} }\n"
         "interface Group_Control_Interface {}\nclass Fonts { const GOOGLE='googlefonts'; const SYSTEM='system'; public static function __callStatic($n,$a){return [];} }\n")
open(W+'/stubs_groups.php', 'w').write("".join(head) + extra + "}\n")
