<?php
define('ABSPATH','/'); define('ELEMENTOR_ASSETS_URL','/'); define('ELEMENTOR_URL','/'); define('ELEMENTOR_PATH',getenv('ELEMENTOR_SRC').'/'); define('ELEMENTOR_VERSION','4.4.0');
foreach(['__','esc_html__','esc_attr__','esc_html','esc_attr','esc_url','wp_kses_post','sanitize_text_field','esc_js'] as $f) eval("function $f(\$t,\$d=null){return \$t;}");
function _x($t,$c,$d=null){return $t;} function esc_html_x($t,$c,$d=null){return $t;} function esc_attr_x($t,$c,$d=null){return $t;}
function _n($s,$p,$n,$d=null){return $s;} function esc_html_e($t,$d=null){} function _e($t,$d=null){}
function is_rtl(){return false;} function apply_filters($h,$v,...$a){return $v;} function do_action(...$a){} function get_option($k,$d=false){return $d;}
function wp_parse_args($a,$d=[]){return array_merge((array)$d,(array)$a);} function admin_url($p=''){return '/wp-admin/'.$p;} function home_url($p=''){return '/'.$p;}
function is_admin(){return false;} function current_user_can(...$a){return false;} function wp_json_encode($v,$f=0){return json_encode($v,$f);} function get_post_types(...$a){return [];} function wp_get_registered_image_subsizes(){return [];} function get_intermediate_image_sizes(){return [];}
function wp_create_nonce($a=''){return 'n';} function get_locale(){return 'en_US';} function get_current_user_id(){return 0;} function is_user_logged_in(){return false;} function get_theme_support($x){return false;} function wp_doing_ajax(){return false;}
function add_action(...$a){} function add_filter(...$a){}
