from pathlib import Path
import json, hashlib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent / 'datos'
SEED = 20260909
catalog = {}

def write(unit, name, df, meta):
    folder=ROOT/unit; folder.mkdir(parents=True,exist_ok=True)
    assert set(df.columns)==set(meta), (unit,name,set(df.columns)^set(meta))
    df.to_csv(folder/name,index=False,encoding='utf-8',float_format='%.4f',na_rep='NA')
    rows=[]
    for col in df:
        desc,role,when,units=meta[col]
        rows.append(dict(archivo=name,variable=col,descripcion=desc,rol=role,disponibilidad=when,unidad=units,tipo=str(df[col].dtype),faltantes=int(df[col].isna().sum())))
    catalog.setdefault(unit,[]).extend(rows)

def m(desc, units='sin unidad', role='predictor', when='al corte'):
    return (desc,role,when,units)

def run():
    catalog.clear()
    rng=np.random.default_rng(SEED)
    n=360; center=np.tile(['Norte','Centro','Sur'],120); method=rng.permutation(np.repeat(['Actual','Guiado','Balanceado'],120))
    lines=rng.poisson(28,n)+3; distance=rng.uniform(100,850,n); shift=rng.choice(['Manana','Tarde'],n)
    common=18+.25*lines+.008*distance+np.where(center=='Sur',1.5,0)+np.where(shift=='Tarde',1,0)
    before=common+rng.normal(0,2,n); effect=np.select([method=='Guiado',method=='Balanceado'],[2,3.8],default=0)
    after=common-effect+rng.normal(0,1.2+.025*lines,n);after[[19,167,298]]+=12
    late=(after>32).astype(int); alarm=(rng.random(n)<np.where(late==1,.84,.13)).astype(int)
    df=pd.DataFrame(dict(lote_id=[f'L{i+1:04d}' for i in range(n)],centro=center,turno=shift,metodo=method,lineas_pedido=lines,distancia_m=distance,tiempo_antes_min=before,tiempo_despues_min=after,incumple_sla=late,alarma_previa=alarm,demanda_repuestos=rng.poisson(2.4,n),costo_final_clp=12000+300*after+4000*late))
    meta={'lote_id':m('Lote de ensayo independiente; ambas mediciones usan el mismo lote','id','identificador'),'centro':m('Centro del ensayo','categoria','contexto'),'turno':m('Turno del ensayo','categoria','contexto'),'metodo':m('Metodo asignado aleatoriamente, 120 lotes por nivel','categoria','tratamiento'),'lineas_pedido':m('Lineas del lote conocidas antes de preparar','lineas'),'distancia_m':m('Recorrido planificado','m'),'tiempo_antes_min':m('Tiempo del lote bajo procedimiento de referencia','min','referencia','antes de aplicar metodo'),'tiempo_despues_min':m('Tiempo observado aplicando metodo asignado','min','respuesta','despues'),'incumple_sla':m('1 si tiempo_despues_min supera 32','0/1','respuesta','despues'),'alarma_previa':m('Alerta de demora disponible antes de ejecutar','0/1'),'demanda_repuestos':m('Repuestos demandados por el lote','unidades','respuesta','despues'),'costo_final_clp':m('Costo realizado; no usar para predecir demora','CLP','excluir_fuga','despues')}
    write('Unidad_0_Fundamentos','lotes_piloto.csv',df,meta)

    rng=np.random.default_rng(SEED+1)
    def capacity(n, new=False):
        orders=rng.poisson(150 if not new else 185,n); units=np.rint(orders*rng.uniform(1.5,3.5,n)).astype(int);lines=np.rint(orders*rng.uniform(.9,1.4,n)).astype(int)
        distance=rng.uniform(400,2200,n);occ=rng.uniform(35,92,n);staff=rng.integers(7,18,n); shift=rng.choice(['Manana','Tarde'],n)
        centers=np.tile([f'C{i}' for i in range(1,9)],n//8+1)[:n] if not new else np.repeat('C9',n)
        target=6+.025*orders+.007*units+.0008*distance-.65*np.minimum(staff,12)+.075*np.maximum(orders-150,0)+.010*(occ-60)**2+.008*orders*(shift=='Tarde')+rng.normal(0,1.5,n)+(2.5 if new else 0)
        z={'registro_id':[f'{"N" if new else "R"}{i+1:04d}' for i in range(n)],'centro':centers,'turno':shift,'pedidos':orders,'unidades':units,'lineas':lines,'distancia_m':distance,'ocupacion_pct':occ,'operarios':staff,'urgentes_pct':rng.uniform(0,30,n),'promocion':rng.integers(0,2,n),'carga_proxy_1':orders+rng.normal(0,3,n),'carga_proxy_2':orders+rng.normal(0,5,n),'horas_persona':target,'costo_cierre_clp':target*7500+rng.normal(0,1500,n)}
        for j in range(1,5):z[f'ruido_{j}']=rng.normal(0,1,n)
        d=pd.DataFrame(z);d.loc[rng.choice(n,int(n*.04),False),'distancia_m']=np.nan;d.loc[rng.choice(n,int(n*.025),False),'ocupacion_pct']=np.nan
        return d
    d=capacity(1440);d.insert(1,'fecha',np.repeat(pd.date_range('2026-01-01',periods=180).strftime('%Y-%m-%d'),8));d['rol_particion']=np.repeat(['entrenamiento','validacion','prueba'],[960,240,240])
    md={'registro_id':m('Centro-turno diario; clave unica','id','identificador'),'fecha':m('Fecha de corte al inicio del turno','AAAA-MM-DD','particion'),'centro':m('Centro de distribucion','categoria'),'turno':m('Turno planificado','categoria'),'pedidos':m('Pedidos confirmados','pedidos'),'unidades':m('Unidades confirmadas','unidades'),'lineas':m('Lineas confirmadas','lineas'),'distancia_m':m('Recorrido planificado; puede faltar','m'),'ocupacion_pct':m('Ocupacion inicial de almacenamiento; puede faltar','porcentaje'),'operarios':m('Dotacion planificada','personas'),'urgentes_pct':m('Fraccion urgente de pedidos','porcentaje'),'promocion':m('Promocion anunciada','0/1'),'carga_proxy_1':m('Indicador redundante de carga','indice'),'carga_proxy_2':m('Segundo indicador redundante de carga','indice'),'horas_persona':m('Trabajo efectivamente requerido','horas-persona','respuesta','cierre del turno'),'costo_cierre_clp':m('Costo posterior altamente asociado con respuesta','CLP','excluir_fuga','cierre del turno'),'rol_particion':m('Separacion temporal fijada; no predictor','categoria','particion')}
    for j in range(1,5):md[f'ruido_{j}']=m('Indicador auxiliar sin significado operacional','indice')
    for role,filename in [('entrenamiento','entrenamiento.csv'),('validacion','validacion.csv'),('prueba','prueba_final.csv')]:write('Unidad_1_Regularizacion',filename,d[d.rol_particion==role],md)
    new=capacity(30,True);new.insert(1,'fecha',pd.date_range('2026-07-01',periods=30).strftime('%Y-%m-%d'));new['rol_particion']='transportabilidad';write('Unidad_1_Regularizacion','centro_nuevo.csv',new,md)

    rng=np.random.default_rng(SEED+2);n=1200
    queue=rng.poisson(6,n);docks=rng.integers(2,7,n);weight=rng.uniform(2,24,n);docs=rng.binomial(1,.2,n);terminal=rng.choice(['Norte','Centro','Sur'],n);staff=rng.integers(4,15,n)
    wait=np.maximum(.5,3+2.8*np.maximum(queue-docks,0)+.2*weight+5*docs+6*((queue>6)&(docks<3))+.06*(staff-9)**2+rng.normal(0,1.2+.15*queue,n))
    d=pd.DataFrame(dict(ventana_id=[f'V{i+1:04d}' for i in range(n)],terminal=terminal,camiones_cola=queue,muelles_activos=docks,peso_t=weight,revision_documental=docs,operarios=staff,prioridad=rng.binomial(1,.15,n),cola_proxy=queue+rng.normal(0,.3,n),codigo_aleatorio=rng.permutation(n)+1000,espera_min=wait,costo_espera_real_clp=wait*1800+rng.normal(0,100,n)))
    md={'ventana_id':m('Ventana independiente; un camion evaluado por ventana','id','identificador'),'terminal':m('Terminal observado','categoria'),'camiones_cola':m('Camiones en cola al llegar','camiones'),'muelles_activos':m('Muelles disponibles','muelles'),'peso_t':m('Peso declarado de carga','t'),'revision_documental':m('Necesidad de revision conocida al llegar','0/1'),'operarios':m('Dotacion disponible','personas'),'prioridad':m('Servicio prioritario contratado','0/1'),'cola_proxy':m('Medicion redundante de cola','indice'),'codigo_aleatorio':m('Identificador numerico arbitrario; usar solo en auditoria de importancia','codigo','identificador'),'espera_min':m('Espera realizada hasta entrar al muelle','min','respuesta','despues'),'costo_espera_real_clp':m('Costo realizado despues de esperar','CLP','excluir_fuga','despues')}
    for sl,fn in [(slice(0,900),'desarrollo.csv'),(slice(900,None),'prueba_final.csv')]:write('Unidad_2_Ensamble',fn,d.iloc[sl],md)

    rng=np.random.default_rng(SEED+3);n=1800;queue=rng.poisson(6,n);dist=rng.uniform(5,180,n);slack=rng.uniform(5,40,n);docs=rng.binomial(1,.18,n);urgent=rng.binomial(1,.22,n)
    eta=-2.2+.10*queue+.007*dist+.8*docs+.6*urgent-.06*slack+.9*((queue>8)&(slack<15))
    prob=1/(1+np.exp(-eta));target=rng.binomial(1,prob)
    d=pd.DataFrame(dict(pedido_id=[f'P{i+1:04d}' for i in range(n)],semana=np.repeat(np.arange(1,19),100),centro=rng.choice(['Norte','Centro','Sur'],n),canal=rng.choice(['Empresa','Sucursal','Web'],n),camiones_cola=queue,distancia_km=dist,holgura_min=slack,revision_documental=docs,urgente=urgent,incidencias_previas=rng.poisson(1.2,n),carga_proxy=queue+rng.normal(0,.4,n),atraso=target,compensacion_real_clp=target*(120000+rng.normal(0,8000,n))))
    d.loc[rng.choice(n,54,False),'distancia_km']=np.nan
    md={'pedido_id':m('Pedido evaluado antes de despachar','id','identificador'),'semana':m('Semana de corte; 100 pedidos por semana','semana','particion'),'centro':m('Centro responsable','categoria'),'canal':m('Canal de solicitud','categoria'),'camiones_cola':m('Cola conocida','camiones'),'distancia_km':m('Distancia planificada; puede faltar','km'),'holgura_min':m('Holgura planificada contra promesa de entrega','min'),'revision_documental':m('Revision requerida conocida','0/1'),'urgente':m('Servicio urgente contratado','0/1'),'incidencias_previas':m('Incidencias del proveedor antes del corte','conteo'),'carga_proxy':m('Proxy correlacionado de la cola','indice'),'atraso':m('1 si el pedido incumple su promesa','0/1','respuesta','al entregar'),'compensacion_real_clp':m('Compensacion conocida despues; excluir','CLP','excluir_fuga','al entregar')}
    for sl,fn in [(slice(0,1200),'entrenamiento.csv'),(slice(1200,1500),'validacion.csv'),(slice(1500,None),'prueba_final.csv')]:write('Unidad_3_Clasificacion',fn,d.iloc[sl],md)
    n=1000;sen=rng.poisson(1.4,(n,3));scores=np.c_[.9*sen[:,0],.9*sen[:,1]-.4,.9*sen[:,2]-.7]+rng.normal(0,.8,(n,3));probs=np.exp(scores-scores.max(axis=1,keepdims=True));probs/=probs.sum(axis=1,keepdims=True);cls=np.array([rng.choice(3,p=p) for p in probs])
    r=pd.DataFrame(dict(reclamo_id=[f'C{i+1:04d}' for i in range(n)],senales_entrega=sen[:,0],senales_factura=sen[:,1],senales_producto=sen[:,2],contactos_previos=rng.poisson(2,n),canal=rng.choice(['Web','Telefono'],n),clase=np.array(['Entrega','Facturacion','Producto'])[cls],rol_particion=np.repeat(['entrenamiento','validacion','prueba'],[700,150,150])))
    rm={'reclamo_id':m('Reclamo independiente','id','identificador'),'senales_entrega':m('Conteo de incidencias declaradas al abrir, relativas a entrega','conteo'),'senales_factura':m('Conteo declarado sobre facturacion','conteo'),'senales_producto':m('Conteo declarado sobre producto','conteo'),'contactos_previos':m('Contactos anteriores a apertura','conteo'),'canal':m('Canal de apertura','categoria'),'clase':m('Equipo al que finalmente correspondio resolver','categoria','respuesta','resolucion'),'rol_particion':m('Particion fija independiente del target','categoria','particion')}
    write('Unidad_3_Clasificacion','reclamos_multiclase.csv',r,rm)

    rng=np.random.default_rng(SEED+4);n=720;g=rng.choice(4,n,p=[.32,.28,.25,.15]);orders=np.maximum(1,rng.normal(np.array([4,12,22,16])[g],np.array([2,4,5,7])[g]));ticket=np.maximum(.05,rng.normal(np.array([.25,.7,1.6,2.7])[g],np.array([.10,.3,.5,1.0])[g]));recency=np.clip(rng.normal(np.array([35,15,8,22])[g],12),1,90);margin=np.clip(rng.normal(np.array([18,26,20,35])[g],6),3,55);returns=np.clip(rng.normal(np.array([2,6,3,9])[g],2),0,25)
    d=pd.DataFrame(dict(cliente_id=[f'CL{i+1:04d}' for i in range(n)],pedidos_mes=orders,ticket_mclp=ticket,recencia_dias=recency,margen_pct=margin,devoluciones_pct=returns,variabilidad_pedidos=np.clip(rng.normal(.3,.15,n),.03,.9),canal=rng.choice(['Digital','Ejecutivo','Mixto'],n),contrato=rng.binomial(1,.55,n),region=rng.choice(['Norte','Centro','Sur'],n)))
    d.loc[rng.choice(n,12,False),'ticket_mclp']*=4
    d.loc[rng.choice(n,22,False),'margen_pct']=np.nan
    md={'cliente_id':m('Identificador estable del cliente','id','identificador'),'pedidos_mes':m('Promedio mensual en los seis meses previos','pedidos/mes'),'ticket_mclp':m('Ticket medio','millones de CLP'),'recencia_dias':m('Dias desde ultima compra','dias'),'margen_pct':m('Margen comercial medio; puede faltar','porcentaje'),'devoluciones_pct':m('Porcentaje de pedidos devueltos','porcentaje'),'variabilidad_pedidos':m('Coeficiente de variacion mensual','razon'),'canal':m('Canal habitual','categoria'),'contrato':m('Contrato comercial vigente','0/1'),'region':m('Region de atencion','categoria')}
    write('Unidad_4_Clustering','clientes_enero.csv',d,md)
    july=d.copy();july['pedidos_mes']=np.maximum(1,july.pedidos_mes*rng.lognormal(.05,.15,n));july['ticket_mclp']*=rng.lognormal(.03,.10,n);july['recencia_dias']=np.clip(july.recencia_dias+rng.normal(0,7,n),1,100);july.loc[660:,'cliente_id']=[f'CL{i:04d}' for i in range(721,781)]
    write('Unidad_4_Clustering','clientes_julio.csv',july,md)
    abandon=rng.binomial(1,1/(1+np.exp(-(-3+.05*recency+.035*returns))))
    ext=pd.DataFrame(dict(cliente_id=d.cliente_id,abandono_semestre=abandon,margen_semestre_mclp=np.maximum(0,orders*ticket*6*np.nan_to_num(margin,nan=24)/100+rng.normal(0,2,n))))
    em={'cliente_id':m('Cliente de enero; clave para unir','id','identificador'),'abandono_semestre':m('Abandono observado despues de enero; solo evaluacion externa','0/1','evaluacion_externa','julio'),'margen_semestre_mclp':m('Margen observado del semestre; nunca entrada del clustering de enero','millones de CLP','evaluacion_externa','julio')}
    write('Unidad_4_Clustering','resultados_semestre.csv',ext,em)

    for unit,rows in catalog.items():
        pd.DataFrame(rows).to_csv(ROOT/unit/'diccionario.csv',index=False,encoding='utf-8')
        main={'Unidad_0_Fundamentos':'lotes_piloto.csv','Unidad_1_Regularizacion':'entrenamiento.csv','Unidad_2_Ensamble':'desarrollo.csv','Unidad_3_Clasificacion':'entrenamiento.csv','Unidad_4_Clustering':'clientes_enero.csv'}[unit]
        (ROOT/unit/'inicio.R').write_text('# Abra R en esta carpeta. Este archivo solo carga y audita; no resuelve los desafios.\nset.seed(20260909)\ndatos <- read.csv("'+main+'", na.strings="NA", fileEncoding="UTF-8", stringsAsFactors=FALSE)\ndiccionario <- read.csv("diccionario.csv", fileEncoding="UTF-8")\nstr(datos)\ncolSums(is.na(datos))\nstopifnot(nrow(datos)>0)\n# Consulte los ejercicios 41--50 y el instructivo de la guia antes de abrir prueba final.\n',encoding='utf-8')
    for unit in catalog:
        starter=ROOT/unit/'inicio.R'
        starter.write_text(starter.read_text(encoding='utf-8').replace('set.seed(20260909)',f'set.seed({SEED+int(unit.split("_")[1])})'),encoding='utf-8')
    manifest=[]
    for f in sorted(ROOT.glob('*/*.csv')):
        frame=pd.read_csv(f);manifest.append(dict(archivo=str(f.relative_to(ROOT)),filas=len(frame),columnas=len(frame.columns),sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
    (ROOT/'manifest.json').write_text(json.dumps({'semilla':SEED,'archivos':manifest},indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
