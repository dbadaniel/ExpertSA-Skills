<?php
require __DIR__.'/wp.php'; require getenv('WORK').'/stubs_gen.php';
$files = array_slice($argv,1); $out=[];
require_once getenv('ELEMENTOR_SRC').'/includes/widgets/traits/button-trait.php';
foreach($files as $f){ $before=get_declared_classes(); try { require_once $f; } catch(\Throwable $e){ fwrite(STDERR,"LOAD $f: ".$e->getMessage()."\n"); continue; }
  foreach(array_diff(get_declared_classes(),$before) as $cls){ $r=new ReflectionClass($cls); if($r->isAbstract()||!$r->hasMethod('register_controls')) continue;
    try{ $o=$r->newInstanceWithoutConstructor(); if($r->hasProperty('active_kit')){ $p=$r->getProperty('active_kit'); $p->setAccessible(true); $p->setValue($o,new \Elementor\Blackhole()); } $m=$r->getMethod('register_controls'); $m->setAccessible(true); $m->invoke($o);
      $name = $r->hasMethod('get_name') ? (function() use($o){ try{ return $o->get_name(); }catch(\Throwable $e){ return null; } })() : null;
      $out[$cls]=['file'=>basename($f),'name'=>$name,'controls'=>array_values($o->cap)];
    } catch(\Throwable $e){ fwrite(STDERR,"RUN $cls: ".$e->getMessage()." @".$e->getFile().":".$e->getLine()."\n"); $out[$cls]=['file'=>basename($f),'partial'=>true,'controls'=>array_values($o->cap??[])]; } } }
echo json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES|JSON_PARTIAL_OUTPUT_ON_ERROR);
