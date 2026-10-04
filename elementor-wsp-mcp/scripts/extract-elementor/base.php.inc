class Blackhole implements \ArrayAccess, \IteratorAggregate, \Countable {
  public function __call($n,$a){ if (preg_match('/^(is_|has_|can_)/',$n)) return false; if (preg_match('/^get_.*s$|_list$|breakpoints|devices|config/',$n)) return []; return new Blackhole(); }
  public function __get($n){ return new Blackhole(); }
  public function __toString(){ return ''; }
  public function offsetExists($o):bool{return false;} public function offsetGet($o):mixed{return new Blackhole();} public function offsetSet($o,$v):void{} public function offsetUnset($o):void{}
  public function getIterator():\Iterator{ return new \ArrayIterator([]); } public function count():int{return 0;}
}
class Plugin { public static $instance; }
Plugin::$instance = new Blackhole();
class Utils { public static function __callStatic($n,$a){ if (preg_match('/^(is_|has_)/',$n)) return false; return ''; } }
class Icons_Manager { public static function __callStatic($n,$a){ return $n==='is_migration_allowed'; } }
class Embed { public static function __callStatic($n,$a){ return ''; } }
class Shapes { const FILTER_EXCLUDE='exclude'; const FILTER_INCLUDE='include'; public static function __callStatic($n,$a){ return []; } }
trait Capture {
  public $cap = []; public $sec=null; public $tab='content'; public $ctab=null; public $ctabs=null;
  function start_controls_section($id,$a=[]){ $this->sec=['id'=>$id,'label'=>$a['label']??$id]; $this->tab=$a['tab']??'content'; }
  function end_controls_section(){ $this->sec=null; }
  function start_controls_tabs($id,$a=[]){ $this->ctabs=$id; } function end_controls_tabs(){ $this->ctabs=null; }
  function start_controls_tab($id,$a=[]){ $this->ctab=$a['label']??$id; } function end_controls_tab(){ $this->ctab=null; }
  function start_popover(){} function end_popover(){}
  function start_injection($a=[]){} function end_injection(){}
  function rec($kind,$id,$a){ $this->cap[$id]=['kind'=>$kind,'id'=>$id,'args'=>$a,'section'=>$this->sec,'tab'=>$this->tab,'state'=>$this->ctab]; return true; }
  function add_control($id,$a=[],$o=[]){ return $this->rec('control',$id,$a); }
  function add_responsive_control($id,$a=[],$o=[]){ return $this->rec('responsive',$id,$a); }
  function add_group_control($type,$a=[],$o=[]){ return $this->rec('group:'.$type,$a['name']??$type,$a); }
  function update_control($id,$a=[],$o=[]){ if(isset($this->cap[$id])) $this->cap[$id]['args']=array_replace_recursive($this->cap[$id]['args'],$a); return true; }
  function update_responsive_control($id,$a=[],$o=[]){ return $this->update_control($id,$a); }
  function update_group_control($id,$a=[],$o=[]){ return $this->update_control($id,$a); }
  function remove_control($id){ unset($this->cap[$id]); } function remove_responsive_control($id){ unset($this->cap[$id]); }
  function get_controls($id=null){ if($id===null) return array_map(fn($c)=>$c['args'],$this->cap); return $this->cap[$id]['args']??null; }
  function get_controls_settings(){ return []; }
  function get_group_name(){ return 'widget'; } function get_id(){ return 'x'; }
  function get_settings($k=null){ return null; } function get_settings_for_display($k=null){ return null; }
  function __call($n,$a){ if (preg_match('/^(is_|has_)/',$n)) return false; return null; }
  function get_stack(){ return []; }
}
abstract class Element_Base { use Capture; public function __construct($d=[],$a=null){} }
abstract class Widget_Base extends Element_Base { }
class Repeater { use Capture; public function __construct($d=[],$a=null){} public function get_controls($id=null){ return array_values(array_map(fn($c)=>$c,$this->cap)); } }
