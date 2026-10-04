<?php
require __DIR__.'/wp.php'; require getenv('WORK').'/stubs_groups.php';
$out=[];
foreach(glob(getenv('ELEMENTOR_SRC').'/includes/controls/groups/*.php') as $f){ if(basename($f)==='base.php') continue; $before=get_declared_classes();
  try{ require_once $f; }catch(\Throwable $e){ fwrite(STDERR,"LOAD $f ".$e->getMessage()."\n"); continue; }
  foreach(array_diff(get_declared_classes(),$before) as $cls){ $r=new ReflectionClass($cls); if($r->isAbstract()||!$r->hasMethod('init_fields')) continue;
    try{ $o=$r->newInstanceWithoutConstructor(); $m=$r->getMethod('init_fields'); $m->setAccessible(true); $fields=$m->invoke($o);
      $type=$r->getMethod('get_type')->invoke(null); $out[$type]=$fields; }catch(\Throwable $e){ fwrite(STDERR,"RUN $cls ".$e->getMessage()." @".$e->getLine()."\n"); } } }
echo json_encode($out,JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES|JSON_PARTIAL_OUTPUT_ON_ERROR);
