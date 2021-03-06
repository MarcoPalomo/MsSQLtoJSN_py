#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, csv, pymssql, jsonimport zipfile, re, fnmatch
import logging.configlogging.config.fileConfig('logging.ini')
with open('./__job_parameters.json', 'r') as fichier:
  data = json.load(fichier)        
  ficIn = data['infile']        
  srv = data['GLOBAL']['SQL04']        
  usr = data['GLOBAL']['sa_user']        
  passwd = data['GLOBAL']['sa_password']
  class MsSql:    
    ''' Paramètres MsSql '''    
    server = srv    
    user = usr    
    password = passwd
    #cheminZip =''ficZip = zipfile.ZipFile(ficIn, 'r')
    #ficZip = zipfile.ZipFile('IDFIDT.zip')
    for fich in ficZip.namelist():    
      if 'csv' in fich:        
        ficCsv = fich        
        breakficPath = r"\\prod1\no_std\Maileva"
        #ficPath = os.path.dirname(__file__)+'/'+ficCsvos.path.join('.', ficPath, ficCsv)ficZip.extract(ficCsv, './')ficZip.close()
        def requete():
          cnx = pymssql.connect(MsSql().server, MsSql().user, MsSql().password, '', as_dict=True)        
          cur = cnx.cursor()        
          cur.execute('SET DATEFORMAT dmy')        
          cnx.commit()       
          sqlrequest = ("bulk insert [0051-Piece-PROD].[dbo].[T_PurgeMaileva] from '"+ficPath+ r".\\"+ficCsv+ r"' with (FIRSTROW = 2, FORMATFILE = '\\prod1\no_std\Maileva\dossier-PurgeMaileva.fmt' ,MAXERRORS=0)")        
          cur.execute(sqlrequest)        
          cnx.commit()        
          cnx.close()
          
        logging.info('Debut des actions...')try:
          requete()        #1/0        
          logging.info('Donnees inserees dans la base')
          except Exception as e:        
            logging.error('Erreur !')        
            logging.exception("Explication du message d'erreur")
