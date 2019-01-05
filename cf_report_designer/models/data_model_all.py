# -*- coding: utf-8 -*-
# 康虎软件工作室
# http://www.khcloud.net
# QQ: 360026606
# wechat: 360026606
#--------------------------
#
import os
import sys
import logging
import string
try :
 import simplejson as json
except ImportError :
 import json
 if 64 - 64: i11iIiiIii
from lxml import etree
try :
 import xml . etree . cElementTree as ET
except ImportError :
 import xml . etree . ElementTree as ET
from xml . dom import minidom
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from odoo . exceptions import AccessError , UserError , ValidationError
from odoo import models , fields , api , _
from Crypto . Cipher import AES
if 73 - 73: II111iiii
IiII1IiiIiI1 = logging . getLogger ( __name__ )
if 40 - 40: oo * OoO0O00
if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
import os
import sys
import hashlib
import string
import random
import base64
from binascii import b2a_hex , a2b_hex
if 24 - 24: II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
from Crypto import Random
from Crypto . Cipher import AES
if 53 - 53: o0oo0o / Oo + o0oo0o / oooO0oo0oOOOO * OoooooooOO + i1I1ii1II1iII
OOo0oO0oooOoO = ( 'C' )
ooO00oOoo = ( 'FS' )
O0OOo = ( 'O' )
II1Iiii1111i = ( 'F' )
i1IIi11111i = ( 'T' )
o000o0o00o0Oo = ( 'S' )
if 80 - 80: OoooooooOO . oo
OOO0O = ( 't' )
oo0ooO0oOOOOo = ( 'u' )
oO000OoOoo00o = ( 'd' )
iiiI11 = ( 'i' )
OOooO = ( 'o72' )
OOoO00o = ( '0' )
II111iiiiII = ( '1' )
if 63 - 63: oOo0O0Ooo % i1IIi
o0oOo0Ooo0O = "1234567890123456"
if 81 - 81: oOoO0oo0OOOo * oooO0oo0oOOOO * OoOO0ooOOoo0O - i1I1ii1II1iII - Ooo00oOo00o
def OooO0OO ( ) :
 return '' . join ( OOo0oO0oooOoO + ooO00oOoo + O0OOo + II1Iiii1111i + i1IIi11111i + o000o0o00o0Oo + OOO0O + oo0ooO0oOOOOo + oO000OoOoo00o + iiiI11 + OOooO + OOoO00o + II111iiiiII )
 if 28 - 28: II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
OO = len ( OooO0OO ( ) )
oO0O = lambda OOoO000O0OO : OOoO000O0OO + ( OO - len ( OOoO000O0OO ) % OO ) * chr ( OO - len ( OOoO000O0OO ) % OO )
iiI1IiI = lambda OOoO000O0OO : OOoO000O0OO [ 0 : - ord ( OOoO000O0OO [ - 1 ] ) ]
if 13 - 13: OoO0O00 . i11iIiiIii - iIii1I11I1II1 - oOo0O0Ooo
class ii1I ( object ) :
 def __init__ ( self , key = False , mode = AES . MODE_CBC ) :
  if 76 - 76: O0 / Ooo00oOo00o . oo * o0000oOoOoO0o - II11iiII
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . oOoO0oo0OOOo % II11iiII / OoooooooOO % iiiiIi11i
  if 75 - 75: i1I1ii1II1iII
  if 97 - 97: i11iIiiIii
  if 32 - 32: OoO0O00 * O0 % iiiiIi11i % o0000oOoOoO0o . oooO0oo0oOOOO
  if 61 - 61: Oo
  if 79 - 79: OoO0O00 + oo - i1I1ii1II1iII
  if 83 - 83: Oo
  if 64 - 64: ooOO00oOo % Oo % i1I1ii1II1iII / oOo0O0Ooo - ooOO00oOo
  if 74 - 74: i1I1ii1II1iII * O0
  if 89 - 89: iiiiIi11i + OoO0O00
  if 3 - 3: i1IIi / oo % OoOO0ooOOoo0O * i11iIiiIii / O0 * OoOO0ooOOoo0O
  if 49 - 49: iiiiIi11i % o0000oOoOoO0o + i1IIi . oo % oOoO0oo0OOOo
  if 48 - 48: OoOO0ooOOoo0O + OoOO0ooOOoo0O / II111iiii / iIii1I11I1II1
  self . key = key or OooO0OO ( )
  self . mode = mode
  if 20 - 20: Ooo00oOo00o
 @ staticmethod
 def get_machine_code ( ) :
  import uuid
  if 77 - 77: oOo0O0Ooo / OoOO0ooOOoo0O
  return str ( uuid . UUID ( int = uuid . getnode ( ) ) )
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / Ooo00oOo00o
 @ staticmethod
 def rand_aes_key ( size = 16 , by_base64 = True , chars = string . ascii_uppercase + string . digits ) :
  I1i1I1II = '' . join ( random . choice ( chars ) for _ in range ( size ) )
  if 45 - 45: o0oo0o . oOo0O0Ooo
  if 83 - 83: iiiiIi11i . iIii1I11I1II1 . oOoO0oo0OOOo
  if 31 - 31: o0000oOoOoO0o . o0000oOoOoO0o - Ooo00oOo00o / ooOO00oOo + Oo * oo
  if 63 - 63: o0oo0o % i1IIi / OoooooooOO - OoooooooOO
  if 8 - 8: oOo0O0Ooo
  if 60 - 60: OoOO0ooOOoo0O / OoOO0ooOOoo0O
  return base64 . b64encode ( I1i1I1II ) if by_base64 else I1i1I1II
  if 46 - 46: o0000oOoOoO0o * II11iiII - ooOO00oOo * iiiiIi11i - o0oo0o
  if 83 - 83: OoooooooOO
 def encrypt ( self , text ) :
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  self . ciphertext = Iii111II . encrypt ( oO0O ( text ) )
  if 9 - 9: ooOO00oOo
  return base64 . b64encode ( self . ciphertext )
  if 33 - 33: Oo . i1I1ii1II1iII
  if 58 - 58: II11iiII * i11iIiiIii / oOo0O0Ooo % o0oo0o - oOoO0oo0OOOo / iiiiIi11i
 def decrypt ( self , text ) :
  ii11i1 = base64 . b64decode ( text )
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  IIIii1II1II = Iii111II . decrypt ( ii11i1 )
  return IIIii1II1II
  if 42 - 42: o0000oOoOoO0o + iiiiIi11i
  if 76 - 76: o0oo0o - ooOO00oOo
from Crypto import Random
from Crypto . Hash import SHA
from Crypto . Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto . Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto . PublicKey import RSA
if 70 - 70: Oo
class oOO ( ) :
 if 10 - 10: oOo0O0Ooo * i1I1ii1II1iII . OoOO0ooOOoo0O + II111iiii - Oo * i1IIi
 if 56 - 56: Ooo00oOo00o * oooO0oo0oOOOO * II111iiii
 if 80 - 80: Ooo00oOo00o * II111iiii % II111iiii
 if 59 - 59: iIii1I11I1II1 + oo - Ooo00oOo00o - oo + II11iiII / oOoO0oo0OOOo
 if 24 - 24: OoOO0ooOOoo0O . i1I1ii1II1iII % II11iiII + Oo % oOo0O0Ooo
 if 4 - 4: oooO0oo0oOOOO - ooOO00oOo * oOo0O0Ooo - OoOO0ooOOoo0O
 if 41 - 41: oOo0O0Ooo . oo * iiiiIi11i % oooO0oo0oOOOO
 if 86 - 86: oo + o0000oOoOoO0o % i11iIiiIii * iiiiIi11i . Oo * OoOO0ooOOoo0O
 if 44 - 44: iiiiIi11i
 if 88 - 88: o0oo0o % o0000oOoOoO0o . II111iiii
 if 38 - 38: Ooo00oOo00o
 if 57 - 57: O0 / iiiiIi11i * o0oo0o / oOo0O0Ooo . II111iiii
 if 26 - 26: i1I1ii1II1iII
 if 91 - 91: ooOO00oOo . oOoO0oo0OOOo + ooOO00oOo - i1I1ii1II1iII / OoooooooOO
 if 39 - 39: oOoO0oo0OOOo / Oo - II111iiii
 def __init__ ( self , pri_key = 'pri.pem' , pub_key = 'pub.pem' , key_path = os . path . abspath ( os . path . dirname ( __file__ ) ) ) :
  self . KEY_PRIVATE = pri_key
  self . KEY_PUBLIC = pub_key
  self . KEY_PATH = key_path
  if 98 - 98: oOoO0oo0OOOo / OoOO0ooOOoo0O % iiiiIi11i . oOo0O0Ooo
 def gen_key_pair ( self ) :
  if 91 - 91: iiiiIi11i % OoO0O00
  O0O0O0OoOO = Random . new ( ) . read
  if 74 - 74: II111iiii
  oO0 = RSA . generate ( 1024 , O0O0O0OoOO )
  if 54 - 54: II111iiii % oOo0O0Ooo % OoOO0ooOOoo0O % iIii1I11I1II1 + iIii1I11I1II1 * Oo
  if 87 - 87: Oo * OoO0O00 % i11iIiiIii % oOo0O0Ooo - II11iiII
  O0ooo0O0oo0 = oO0 . exportKey ( )
  if 91 - 91: iIii1I11I1II1 + o0oo0o
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE , 'w' ) as i1i :
   i1i . write ( O0ooo0O0oo0 )
   if 46 - 46: o0oo0o % OoOO0ooOOoo0O + ooOO00oOo . oOo0O0Ooo . ooOO00oOo
  oO00o0 = oO0 . publickey ( ) . exportKey ( )
  with open ( self . KEY_PATH + "/" + self . KEY_PUBLIC , 'w' ) as i1i :
   i1i . write ( oO00o0 )
   if 55 - 55: OoO0O00 + iIii1I11I1II1 / oOo0O0Ooo * iiiiIi11i - i11iIiiIii - o0000oOoOoO0o
 def decrypt_str ( self , encrypt_text ) :
  if 25 - 25: oOoO0oo0OOOo
  Ii1i = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( Ii1i ) :
   raise Exception ( "Decrypt key not exist or invalid!" )
   if 15 - 15: oooO0oo0oOOOO . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - o0000oOoOoO0o . i1IIi
  O0O0O0OoOO = Random . new ( ) . read
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE ) as i1i :
   i1 = i1i . read ( )
   O0OoO0o = RSA . importKey ( i1 )
   OO0oOO0O = Cipher_pkcs1_v1_5 . new ( O0OoO0o )
   IIIii1II1II = OO0oOO0O . decrypt ( base64 . b64decode ( encrypt_text ) , O0O0O0OoOO )
   return IIIii1II1II
   if 91 - 91: O0
 def encrypt_str ( self , message ) :
  Ii1i = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( Ii1i ) :
   raise Exception ( "Encrypt key not exist or invalid!" )
   if 61 - 61: II111iiii
  with open ( Ii1i ) as i1i :
   i1 = i1i . read ( )
   O0OoO0o = RSA . importKey ( i1 )
   OO0oOO0O = Cipher_pkcs1_v1_5 . new ( O0OoO0o )
   O0OOO = base64 . b64encode ( OO0oOO0O . encrypt ( message ) )
   return O0OOO
   if 10 - 10: II11iiII * OoOO0ooOOoo0O % oOo0O0Ooo / oo / oOo0O0Ooo
   if 42 - 42: ooOO00oOo
   if 67 - 67: o0oo0o . i1I1ii1II1iII . O0
   if 10 - 10: oOoO0oo0OOOo % oOoO0oo0OOOo - iIii1I11I1II1 / II11iiII + o0000oOoOoO0o
   if 87 - 87: iiiiIi11i * oOoO0oo0OOOo + II11iiII / iIii1I11I1II1 / i1I1ii1II1iII
   if 37 - 37: i1I1ii1II1iII - Oo * iiiiIi11i % i11iIiiIii - o0oo0o
   if 83 - 83: OoOO0ooOOoo0O / oo
   if 34 - 34: oooO0oo0oOOOO
   if 57 - 57: iiiiIi11i . OoOO0ooOOoo0O . i1IIi
   if 42 - 42: OoOO0ooOOoo0O + oOoO0oo0OOOo % O0
   if 6 - 6: iiiiIi11i
   if 68 - 68: oOo0O0Ooo - ooOO00oOo
IIi = "report_"
ooOOoooooo = "report_"
II1I = "report_"
if 84 - 84: oooO0oo0oOOOO . i11iIiiIii . oooO0oo0oOOOO * oOoO0oo0OOOo - OoOO0ooOOoo0O
if 42 - 42: i11iIiiIii
class I11i1iIII ( models . Model ) :
 _name = 'cf.cfprint.license'
 _description = u'许可证信息'
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - Ooo00oOo00o
 mcode = fields . Char ( string = u'机器码' , default = lambda o00oooO0Oo : ii1I . get_machine_code ( ) , help = u'服务器机器码' )
 license = fields . Binary ( string = u'许可证' , help = u'授权许可证文件，下载后改名为cfprint.lic放到客户端cfprint目录下。' )
 note = fields . Char ( string = u'备注' )
 if 78 - 78: o0000oOoOoO0o % o0oo0o + oOoO0oo0OOOo
 @ api . model
 def create ( self , vals ) :
  vals [ 'mcode' ] = OOooOoooOoOo = ii1I . get_machine_code ( ) or ''
  return super ( I11i1iIII , self ) . create ( vals )
  if 84 - 84: oooO0oo0oOOOO
 @ api . multi
 def write ( self , vals ) :
  vals [ 'mcode' ] = OOooOoooOoOo = ii1I . get_machine_code ( ) or ''
  return super ( I11i1iIII , self ) . write ( vals )
  if 86 - 86: oOo0O0Ooo - o0000oOoOoO0o - ooOO00oOo * i1I1ii1II1iII
class oooo0O0 ( models . Model ) :
 _inherit = 'ir.model'
 if 51 - 51: ooOO00oOo / ooOO00oOo
 def name_get ( self ) :
  return [ ( ooOOO0 . id , '%s(%s)' % ( ooOOO0 . name , ooOOO0 . model ) ) for ooOOO0 in self ]
  if 65 - 65: O0
class oO00OOoO00 ( models . Model ) :
 _name = 'cf.report.define'
 _description = u'报表定义'
 if 40 - 40: oo * o0000oOoOoO0o + II11iiII % i1I1ii1II1iII
 name = fields . Char ( string = u'报表ID' , copy = True , help = u"用一确定报表的唯一ID，只允许英文、数字和下划线。" )
 comment = fields . Char ( string = u'报表中文名称' , copy = True )
 model_id = fields . Many2one ( 'ir.model' , string = u'数据表(model)' , required = True , copy = True , help = u"报表对应的数据表(model)" )
 template_id = fields . Many2one ( 'cf.template' , string = u'报表模板' , copy = True , help = u"该报表使用的打印模板。\n模板如果尚未设计，可以先创建一个模板定义，待生成数据并设计报表模板后再上传到模板库。" )
 company_id = fields . Many2one ( 'res.company' , string = u'所属公司' , default = lambda OOOOOoo0 : OOOOOoo0 . env [ 'res.company' ] . _company_default_get ( '' ) )
 open_print = fields . Boolean ( string = u"是否弹出打印" , default = False )
 use_client_templ = fields . Boolean ( string = u"使用客户端模板" , default = False , help = u"" )
 client_templ_name = fields . Char ( string = u"客户端模板文件名" , help = u"如果设置了使用客户端模板，则在此录入客户端模板路径和文件名" )
 field_ids = fields . One2many ( "cf.report.define.field" , "report_id" , string = u"字段" , help = u"要在报表模板中使用的字段信息" )
 state = fields . Selection ( [ ( 'draft' , u'草稿' ) , ( 'defined' , u'完成报表定义' ) ] , string = u"状态" , default = "draft" )
 note = fields . Text ( string = u"备注" )
 if 49 - 49: O0 . i1I1ii1II1iII
 _sql_constraints = [
 ( 'uniq_name' , 'unique(name)' , _ ( u'报表名称必须唯一!' ) ) ,
 ]
 if 11 - 11: oooO0oo0oOOOO * oo . iIii1I11I1II1 % OoooooooOO + i1I1ii1II1iII
 @ api . model
 def create ( self , vals ) :
  if not vals . get ( "template_id" , False ) :
   OOO = vals . get ( "name" , False )
   oo0OOo0 = vals . get ( "comment" , False )
   if not OOO :
    raise ValidationError ( _ ( u"请先指定报表ID！" ) )
   I11IiI = "cf_templ_%s" % ( ooOOoooooo , OOO . replace ( '.' , '_' ) )
   O0ooO0Oo00o = self . env [ "cf.template" ] . search ( [ ( 'templ_id' , '=' , I11IiI ) ] , limit = 1 )
   if not O0ooO0Oo00o :
    O0ooO0Oo00o = self . env [ "cf.template" ] . create ( {
 "templ_id" : I11IiI ,
 "name" : ( oo0OOo0 or I11IiI ) + "打印模板" ,
 "description" : ( oo0OOo0 or I11IiI ) + "打印模板" ,
 } )
   vals [ "template_id" ] = O0ooO0Oo00o . id
   if 77 - 77: iIii1I11I1II1 * ooOO00oOo
  return super ( oO00OOoO00 , self ) . create ( vals )
  if 95 - 95: oo + i11iIiiIii
 @ api . multi
 def unlink ( self ) :
  for I1Ii in self :
   I1Ii . _remove_report ( )
  return super ( oO00OOoO00 , self ) . unlink ( )
  if 94 - 94: o0000oOoOoO0o - II111iiii . II11iiII % OoOO0ooOOoo0O . i11iIiiIii + O0
 def _get_report_id ( self ) :
  self . ensure_one ( )
  return "%s%s" % ( II1I , self . name )
  if 26 - 26: OoOO0ooOOoo0O - iIii1I11I1II1 - oo / ooOO00oOo . oOo0O0Ooo % iIii1I11I1II1
 def _get_report_name ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( ooOOoooooo , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( ooOOoooooo , self . name . replace ( '.' , '_' ) )
   if 91 - 91: Ooo00oOo00o . iIii1I11I1II1 / iiiiIi11i + i1IIi
 def _get_report_file ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( IIi , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( IIi , self . name . replace ( '.' , '_' ) )
   if 42 - 42: Oo . Ooo00oOo00o . Oo - oOoO0oo0OOOo
 @ api . one
 def _remove_report ( self ) :
  i1ii1I1I1 = self . _get_report_id ( )
  oO = self . _get_report_name ( )
  oO0O0o0Oooo = self . _get_report_file ( )
  if 5 - 5: Oo - II111iiii - OoooooooOO % o0000oOoOoO0o + oo * iIii1I11I1II1
  if 37 - 37: oooO0oo0oOOOO % Oo + oOo0O0Ooo + Ooo00oOo00o * OoOO0ooOOoo0O % O0
  self . env [ "ir.model.data" ] . sudo ( ) . search ( [ ( 'name' , '=' , i1ii1I1I1 ) ] ) . unlink ( )
  if 61 - 61: oo - II11iiII . iiiiIi11i / II11iiII + OoO0O00
  I1i11i = self . env [ 'ir.actions.report' ] . sudo ( ) . search ( [ ( 'report_name' , '=' , oO ) ] )
  for I1Ii in I1i11i :
   I1Ii . unlink_action ( )
   I1Ii . unlink ( )
   if 64 - 64: II11iiII % iIii1I11I1II1 * iiiiIi11i
   if 79 - 79: O0
  self . env [ 'ir.ui.view' ] . search ( [ ( 'key' , '=' , oO ) ] ) . unlink ( )
  if 78 - 78: oOoO0oo0OOOo + II11iiII - o0oo0o
  if 38 - 38: Ooo00oOo00o - iiiiIi11i + iIii1I11I1II1 / oOo0O0Ooo % OoO0O00
  if 57 - 57: ooOO00oOo / Oo
  if 29 - 29: iIii1I11I1II1 + oOo0O0Ooo * ooOO00oOo * II11iiII . oo * oo
  if 7 - 7: oooO0oo0oOOOO * o0oo0o % o0000oOoOoO0o - Ooo00oOo00o
  if 13 - 13: o0000oOoOoO0o . i11iIiiIii
  if 56 - 56: oOoO0oo0OOOo % O0 - oo
  if 100 - 100: o0000oOoOoO0o - O0 % iiiiIi11i * II11iiII + oo
  if 88 - 88: OoooooooOO - ooOO00oOo * O0 * OoooooooOO . OoooooooOO
 def action_retrieve_fields ( self ) :
  if 33 - 33: o0oo0o + i1I1ii1II1iII * iiiiIi11i / iIii1I11I1II1 - oo
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 54 - 54: o0oo0o / II11iiII . iiiiIi11i % i1I1ii1II1iII
  if 57 - 57: i11iIiiIii . oOoO0oo0OOOo - o0000oOoOoO0o - iiiiIi11i + oOo0O0Ooo
  if 63 - 63: oOo0O0Ooo * i1I1ii1II1iII
  for ooiIi1 in self . model_id . field_id :
   OoOOoOooooOOo = self . env [ 'cf.report.define.field' ] . create ( {
 "report_id" : self . id ,
 "model_id" : ooiIi1 . model_id . id ,
 "field_id" : ooiIi1 . id ,
 } )
   if 87 - 87: oo
 def _make_report_defind ( self ) :
  if 58 - 58: oOo0O0Ooo % Ooo00oOo00o
  i1ii1I1I1 = self . _get_report_id ( )
  oO = self . _get_report_name ( )
  oO0O0o0Oooo = self . _get_report_file ( )
  if 50 - 50: o0oo0o . Ooo00oOo00o
  if 97 - 97: O0 + oOo0O0Ooo
  OO0O000 = self . env [ 'ir.actions.report' ]
  iiIiI1i1 = OO0O000 . create ( {
 "name" : self . comment or self . name ,
 "type" : "ir.actions.report" ,
 "binding_type" : "report" ,
 "model" : self . model_id . model ,
 "report_type" : "qweb-html" ,
 "report_name" : oO ,
 "report_file" : oO0O0o0Oooo ,
  "multi" : False ,
 "print_report_name" : self . comment or self . name ,
  "attachment_use" : False ,
 "cf_report_define_id" : self . id ,
 } )
  if iiIiI1i1 :
   self . env [ "ir.model.data" ] . create ( {
 "name" : "action_%s" % ( i1ii1I1I1 ) ,
 "model" : "ir.actions.report" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : iiIiI1i1 . id
 } )
   if 69 - 69: Oo
   iiIiI1i1 . create_action ( )
   if 40 - 40: o0oo0o + OoooooooOO % Ooo00oOo00o - iIii1I11I1II1 . oo
 def _make_templ ( self ) :
  if 48 - 48: Ooo00oOo00o - iiiiIi11i / OoooooooOO
  if 100 - 100: oo / Ooo00oOo00o % II111iiii % OoO0O00 % II11iiII
  O00oO000O0O = "%s%s" % ( ooOOoooooo , self . name . replace ( '.' , '_' ) )
  i1ii1I1I1 = self . _get_report_id ( )
  oO = self . _get_report_name ( )
  oO0O0o0Oooo = self . _get_report_file ( )
  if 18 - 18: i1I1ii1II1iII - II11iiII . o0oo0o . iIii1I11I1II1
  i1I = self . _get_report_name ( False )
  if 78 - 78: OoOO0ooOOoo0O * iIii1I11I1II1 . oo / Ooo00oOo00o - OoooooooOO / o0oo0o
  i1I1IiiIi1i = """<?xml version="1.0"?>
<t t-name="%s">
  <t t-call="cfprint.html_container">
    <t t-raw="show_message"/>
  </t>
<script type="text/javascript">
  <t t-raw="cfprint_json"/>
</script>
</t>
""" % ( i1I )
  if 29 - 29: oo % oo
  Oo0O0 = self . env [ 'ir.ui.view' ]
  if 82 - 82: II111iiii % OoOO0ooOOoo0O / ooOO00oOo + oOo0O0Ooo / Ooo00oOo00o / o0oo0o
  try :
   oOo0OOoO0 = Oo0O0 . create ( {
 "name" : i1ii1I1I1 ,
 "key" : oO ,
 "priority" : 16 ,
 "type" : "qweb" ,
 "arch_db" : i1I1IiiIi1i ,
 "mode" : "primary" ,
 "active" : True ,

   } )
   if oOo0OOoO0 :
    self . env [ "ir.model.data" ] . create ( {
 "name" : i1I ,
 "model" : "ir.ui.view" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : oOo0OOoO0 . id
 } )
    if 11 - 11: oOoO0oo0OOOo . ooOO00oOo * oooO0oo0oOOOO * OoooooooOO + Oo
  except Exception as IiII111i1i11 :
   IiII1IiiIiI1 . error ( "Create report template[%s] failed." % ( oO ) )
   raise IiII111i1i11
   if 40 - 40: Oo * oooO0oo0oOOOO * i11iIiiIii
 def action_generate ( self ) :
  if 57 - 57: Oo
  if 29 - 29: oOo0O0Ooo - oooO0oo0oOOOO * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
  if 74 - 74: o0000oOoOoO0o - oooO0oo0oOOOO / i1I1ii1II1iII * O0 - II11iiII
  self . _remove_report ( )
  if 19 - 19: oo
  if 25 - 25: o0000oOoOoO0o / Oo
  self . _make_report_defind ( )
  if 31 - 31: II11iiII . O0 % oo . Ooo00oOo00o + oooO0oo0oOOOO
  if 71 - 71: o0oo0o . II111iiii
  self . _make_templ ( )
  if 62 - 62: OoooooooOO . OoOO0ooOOoo0O
  self . write ( { "state" : "defined" } )
  if 61 - 61: oOo0O0Ooo - II11iiII - i1IIi
 def action_design ( self ) :
  if 25 - 25: O0 * OoOO0ooOOoo0O + oOoO0oo0OOOo . Ooo00oOo00o . Ooo00oOo00o
  if 58 - 58: oo
  if 53 - 53: i1IIi
  o0OOOoO0 = self . env [ self . model_id . model ] . search ( [ ] , limit = 5 )
  o0OoOo00o0o = [ o00oooO0Oo . id for o00oooO0Oo in o0OOOoO0 ]
  if 41 - 41: Oo % ooOO00oOo - OoO0O00 * o0oo0o * OoO0O00
  if 69 - 69: II11iiII - OoooooooOO + Ooo00oOo00o - OoOO0ooOOoo0O
  i1ii1I1I1 = "cf_report_designer.%s%s" % ( II1I , self . name )
  if 23 - 23: i11iIiiIii
  oO = "cf_report_designer.%s%s" % ( ooOOoooooo , self . name )
  II1iIi11 = { "is_design" : True ,
 "docs" : o0OOOoO0 ,
 "docids" : o0OoOo00o0o ,
 "is_design" : True
 }
  if 12 - 12: o0000oOoOoO0o + i11iIiiIii * iIii1I11I1II1 / oOoO0oo0OOOo . OoOO0ooOOoo0O
  return ( self . env [ 'ir.actions.report' ] . search ( [ ( 'report_name' , '=' , oO ) ] , limit = 1 )
 . with_context ( { 'is_design' : True } )
 . report_action ( o0OoOo00o0o , data = II1iIi11 ) )
  if 5 - 5: i1IIi + oooO0oo0oOOOO / Ooo00oOo00o . i1I1ii1II1iII / OoOO0ooOOoo0O
  if 32 - 32: oo % iIii1I11I1II1 / i1IIi - oo
class I1III1111iIi ( models . Model ) :
 _name = 'cf.report.define.field'
 _description = u'报表字段'
 _order = 'report_id, id'
 if 38 - 38: i1I1ii1II1iII + OoOO0ooOOoo0O / o0oo0o % Oo - oOoO0oo0OOOo
 report_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , required = True , ondelete = 'cascade' , help = u"字段所在的报表定义" )
 model_id = fields . Many2one ( 'ir.model' , string = u"数据表(模型)" , required = True , ondelete = 'cascade' , help = u"字段所在的model" )
 model_name = fields . Char ( related = "model_id.name" , string = u"模型名称" )
 field_id = fields . Many2one ( "ir.model.fields" , string = u"字段" , required = True , ondelete = 'cascade' )
 name = fields . Char ( related = "field_id.name" , string = u'字段名称' , required = True )
 field_description = fields . Char ( related = "field_id.field_description" , string = u'字段说明' )
 ttype = fields . Selection ( related = "field_id.ttype" , string = u'字段类型' )
 parent_field_id = fields . Many2one ( "cf.report.define.field" , string = u"关联上级字段" )
 sub_field_ids = fields . One2many ( "cf.report.define.field" , "parent_field_id" , string = u"下级字段" )
 note = fields . Text ( string = u"备注" )
 if 14 - 14: iiiiIi11i / o0oo0o
 _sql_constraints = [
 ( 'uniq_repoer_model_field' , 'unique(report_id, model_id, field_id)' , u'报表+表+字段必须唯一!' ) ,
 ]
 if 85 - 85: OoOO0ooOOoo0O
 def action_retrieve_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' ) :
   if self . env . get ( self . field_id . relation , "NO" ) == "NO" :
    raise AccessError ( _ ( u"未找到关联字段对应的表（%s），无法获取子表字段！" % ( self . field_id . relation ) ) )
    if 20 - 20: iiiiIi11i % oooO0oo0oOOOO
   III1i1i11i = self . env [ "ir.model" ] . search ( [ ( 'model' , '=' , self . field_id . relation ) ] , limit = 1 )
   if 100 - 100: iiiiIi11i / o0oo0o / oOoO0oo0OOOo
   if 78 - 78: OoO0O00 - Ooo00oOo00o / oOo0O0Ooo
   self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) , ( 'model_id' , '=' , III1i1i11i . id ) ] ) . unlink ( )
   if 10 - 10: i1I1ii1II1iII + OoO0O00 * oOoO0oo0OOOo + iIii1I11I1II1 / o0oo0o / oOoO0oo0OOOo
   for ooiIi1 in III1i1i11i . field_id :
    OoOOoOooooOOo = self . env [ 'cf.report.define.field' ] . create ( {
 "parent_field_id" : self . id ,
 "report_id" : self . report_id . id ,
 "model_id" : ooiIi1 . model_id . id ,
 "field_id" : ooiIi1 . id ,
 } )
    if 42 - 42: oo
 def action_view_sub_fields ( self ) :
  self . ensure_one ( )
  II1i11I = self . env . ref ( 'cf_report_designer.cf_report_define_field_form' ) . id
  return { 'type' : 'ir.actions.act_window' ,
 'res_model' : 'cf.report.define.field' ,
 'view_mode' : 'form' ,
 'views' : [ ( II1i11I , 'form' ) ] ,
 'res_id' : self . id ,
 'target' : 'new' ,
 'limit' : 1000 ,
 'name' : u'从表字段' ,
 'flags' : { 'form' : { 'action_buttons' : False } }
 }
  if 50 - 50: OoooooooOO % OoOO0ooOOoo0O
  if 49 - 49: iiiiIi11i - i11iIiiIii . o0oo0o * o0000oOoOoO0o % i1I1ii1II1iII + i1IIi
  if 71 - 71: Ooo00oOo00o
  if 38 - 38: iiiiIi11i % oOo0O0Ooo + oOoO0oo0OOOo . i11iIiiIii
  if 53 - 53: i11iIiiIii * i1I1ii1II1iII
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . Ooo00oOo00o / II111iiii % OoO0O00
  if 38 - 38: Oo - II11iiII / i1I1ii1II1iII
  if 66 - 66: O0 % oOoO0oo0OOOo + i11iIiiIii . oOo0O0Ooo / o0000oOoOoO0o + oOoO0oo0OOOo
from xml . dom import minidom
import uuid
if 86 - 86: Ooo00oOo00o
i1Iii11Ii1i1 = "<h5 style=\"margin-top: 3rem; text-align: center;\">%s</h4>"
if 59 - 59: OoO0O00 % OoooooooOO . i1I1ii1II1iII / oooO0oo0oOOOO + oo
if 76 - 76: Oo
class OoO0O00O0oo0O ( models . Model ) :
 if 36 - 36: II11iiII + O0 - o0000oOoOoO0o - O0 % OoOO0ooOOoo0O . iiiiIi11i
 _inherit = 'ir.actions.report'
 if 74 - 74: i11iIiiIii . oo
 if 36 - 36: OoooooooOO . ooOO00oOo
 if 56 - 56: OoO0O00 . oOoO0oo0OOOo . oo
 _description = 'Report Action'
 if 39 - 39: O0 + o0oo0o
 cf_report_define_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , help = u"如果是康虎云报表，则保存对应的报表定义。" )
 if 91 - 91: OoooooooOO - iIii1I11I1II1 + oOo0O0Ooo / ooOO00oOo . oOo0O0Ooo + O0
 def _make_cfprint_json ( self , values ) :
  if 26 - 26: oOoO0oo0OOOo - OoooooooOO
  if 11 - 11: oo * iiiiIi11i
  def o000oo ( report_define , model , fields , docs , datas ) :
   if 95 - 95: Oo / Oo
   if 30 - 30: oOoO0oo0OOOo + OoO0O00 / OoO0O00 % oOoO0oo0OOOo . oOoO0oo0OOOo
   def O0O0Oo00 ( lst ) :
    oOoO00o = set ( )
    oO00O0 = [ ]
    for IIi1IIIi in lst :
     O00Ooo = tuple ( IIi1IIIi . items ( ) )
     if O00Ooo not in oOoO00o :
      oOoO00o . add ( O00Ooo )
      oO00O0 . append ( IIi1IIIi )
    return oO00O0
    if 52 - 52: oOoO0oo0OOOo - OoO0O00 + oOoO0oo0OOOo % Ooo00oOo00o
   iI1 = { }
   if 12 - 12: oo . i1IIi + oOo0O0Ooo + II11iiII + oo / i1I1ii1II1iII
   I1i1iiiI1 = model . model . replace ( "." , "_" )
   if 24 - 24: iiiiIi11i / i11iIiiIii + iiiiIi11i
   if 20 - 20: OoOO0ooOOoo0O + o0000oOoOoO0o / O0 % iIii1I11I1II1
   for oOo0O in docs :
    OOO0O00oO = { }
    if 9 - 9: iIii1I11I1II1
    for OoOOoOooooOOo in [ IIi1IIIi for IIi1IIIi in fields if IIi1IIIi . model_id . model == model . model ] :
     try :
      if OoOOoOooooOOo . ttype in [ 'char' ] :
       if OoOOoOooooOOo . name == "type_name" :
        if 31 - 31: Ooo00oOo00o % ooOO00oOo
        if 14 - 14: iiiiIi11i / iiiiIi11i % Oo
        pass
       OOO0O00oO [ OoOOoOooooOOo . name ] = oOo0O [ OoOOoOooooOOo . name ] or ""
       if 56 - 56: oo . O0 + OoO0O00
       if OoOOoOooooOOo . ttype == 'char' and oOo0O [ OoOOoOooooOOo . name ] and len ( oOo0O [ OoOOoOooooOOo . name ] ) > iI1 . get ( OoOOoOooooOOo . name , 0 ) :
        iI1 [ OoOOoOooooOOo . name ] = len ( oOo0O [ OoOOoOooooOOo . name ] )
        if 1 - 1: i1I1ii1II1iII
      elif OoOOoOooooOOo . ttype in [ 'boolean' ] :
       OOO0O00oO [ OoOOoOooooOOo . name ] = oOo0O [ OoOOoOooooOOo . name ]
       if 97 - 97: II11iiII + i1I1ii1II1iII + O0 + i11iIiiIii
      elif OoOOoOooooOOo . ttype in [ 'integer' , 'float' ] :
       OOO0O00oO [ OoOOoOooooOOo . name ] = oOo0O [ OoOOoOooooOOo . name ] if oOo0O [ OoOOoOooooOOo . name ] != None else ""
       if 77 - 77: Ooo00oOo00o / OoooooooOO
      elif OoOOoOooooOOo . ttype == 'datetime' :
       OOO0O00oO [ OoOOoOooooOOo . name ] = oOo0O [ OoOOoOooooOOo . name ] . strftime ( "%Y-%m-%d %H:%M:%S" ) if oOo0O [ OoOOoOooooOOo . name ] else ""
       if 46 - 46: Ooo00oOo00o % iIii1I11I1II1 . i1I1ii1II1iII % i1I1ii1II1iII + i11iIiiIii
      elif OoOOoOooooOOo . ttype == 'binary' :
       Oo00o0OO0O00o = oOo0O [ OoOOoOooooOOo . name ] . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" ) if oOo0O [ OoOOoOooooOOo . name ] else ""
       OOO0O00oO [ OoOOoOooooOOo . name ] = "base64/jpg:%s" % ( Oo00o0OO0O00o )
       if 82 - 82: OoOO0ooOOoo0O + OoooooooOO - i1IIi . i1IIi
      elif OoOOoOooooOOo . ttype in [ "one2many" , "many2many" ] and len ( OoOOoOooooOOo . sub_field_ids ) > 0 :
       iIi1i = oOo0O [ OoOOoOooooOOo . name ]
       I1i11111i1i11 = OoOOoOooooOOo . sub_field_ids
       OOoOOO0 = self . env [ 'ir.model' ] . search ( [ ( 'model' , '=' , OoOOoOooooOOo . field_id . relation ) ] , limit = 1 )
       if iIi1i and len ( iIi1i ) > 0 and I1i11111i1i11 and len ( I1i11111i1i11 ) > 0 and OOoOOO0 :
        o000oo ( report_define , OOoOOO0 , I1i11111i1i11 , iIi1i , datas )
        if 10 - 10: o0oo0o / Oo + i11iIiiIii / o0000oOoOoO0o
      elif OoOOoOooooOOo . ttype in [ 'many2one' ] :
       OOO0O00oO [ OoOOoOooooOOo . name ] = oOo0O [ OoOOoOooooOOo . name ] . id or ""
       OOO0O00oO [ OoOOoOooooOOo . name + "_name" ] = oOo0O [ OoOOoOooooOOo . name ] . name or ""
       if 74 - 74: II11iiII + O0 + i1IIi - i1IIi + II111iiii
       if 83 - 83: oOoO0oo0OOOo - oo + II11iiII
       if len ( OOO0O00oO [ OoOOoOooooOOo . name + "_name" ] ) > iI1 . get ( OoOOoOooooOOo . name + "_name" , 0 ) :
        iI1 [ OoOOoOooooOOo . name + "_name" ] = len ( OOO0O00oO [ OoOOoOooooOOo . name + "_name" ] )
        if 5 - 5: o0000oOoOoO0o
     except Exception as iIi1i1iIi1iI :
      IiII1IiiIiI1 . error ( _ ( u"生成康虎云报表打印数据出错。model: %s, field: %s, Error: %s" ) % ( model . model , OoOOoOooooOOo . name , iIi1i1iIi1iI ) )
      if 26 - 26: OoooooooOO * oo + II11iiII
    if OOO0O00oO :
     if not datas . get ( I1i1iiiI1 , False ) :
      datas [ I1i1iiiI1 ] = { "cols" : [ ] , "rows" : [ ] }
     datas [ I1i1iiiI1 ] [ "rows" ] . append ( OOO0O00oO )
     if 24 - 24: i11iIiiIii % iIii1I11I1II1 + II11iiII / i11iIiiIii
     if 70 - 70: ooOO00oOo * O0 . OoOO0ooOOoo0O + oo . oooO0oo0oOOOO
   for OoOOoOooooOOo in [ IIi1IIIi for IIi1IIIi in fields if IIi1IIIi . model_id . model == model . model ] :
    Ii1iIiII1Ii = "str"
    if OoOOoOooooOOo . ttype in [ "integer" ] :
     Ii1iIiII1Ii = "int"
    elif OoOOoOooooOOo . ttype in [ "float" ] :
     Ii1iIiII1Ii = "float"
    elif OoOOoOooooOOo . ttype in [ "datetime" ] :
     Ii1iIiII1Ii = "date"
    elif OoOOoOooooOOo . ttype in [ "boolean" ] :
     Ii1iIiII1Ii = "boolean"
    elif OoOOoOooooOOo . ttype in [ "binary" ] :
     Ii1iIiII1Ii = "blob"
    elif OoOOoOooooOOo . ttype in [ "many2one" ] :
     Ii1iIiII1Ii = "int"
     if 42 - 42: O0 * o0000oOoOoO0o . OoO0O00 - oo * iIii1I11I1II1
    iII111Ii = 0
    if Ii1iIiII1Ii == "str" :
     iII111Ii = iI1 . get ( OoOOoOooooOOo . name , 20 )
     if 52 - 52: II111iiii % oooO0oo0oOOOO . oOo0O0Ooo * iIii1I11I1II1
    if not datas . get ( I1i1iiiI1 , False ) :
     datas [ I1i1iiiI1 ] = { "cols" : [ ] , "rows" : [ ] }
    datas [ I1i1iiiI1 ] [ "cols" ] . append ( { "type" : Ii1iIiII1Ii , "size" : iII111Ii , "name" : OoOOoOooooOOo . name , "required" : False , "comment" : OoOOoOooooOOo . field_description } )
    if OoOOoOooooOOo . ttype in [ "many2one" ] :
     datas [ I1i1iiiI1 ] [ "cols" ] . append ( { "type" : Ii1iIiII1Ii , "size" : iI1 . get ( OoOOoOooooOOo . name + "_name" , 20 ) , "name" : OoOOoOooooOOo . name + "_name" , "required" : False , "comment" : OoOOoOooooOOo . field_description } )
     if 50 - 50: Oo - o0oo0o * oooO0oo0oOOOO . oOoO0oo0OOOo
   datas [ I1i1iiiI1 ] [ "cols" ] = O0O0Oo00 ( datas [ I1i1iiiI1 ] [ "cols" ] )
   return datas
   if 37 - 37: Oo % i11iIiiIii % II111iiii . O0 . o0000oOoOoO0o
   if 51 - 51: ooOO00oOo - O0 % iiiiIi11i - II111iiii
   if 31 - 31: i1I1ii1II1iII / OoO0O00 - i1I1ii1II1iII - II11iiII
  I1iiIIIi11 = values . get ( "report_define" )
  OOooOoooOoOo = ii1I . get_machine_code ( ) or ''
  Ii1I11ii1i = {
 "template" : "" ,
 "ver" : 4 ,
 "Copies" : 1 ,
 "Duplex" : 0 ,
 "mcode" : OOooOoooOoOo ,
 "Tables" : [ ]
 }
  if 89 - 89: i1I1ii1II1iII . O0 / oOoO0oo0OOOo % oOo0O0Ooo . OoO0O00
  IiiI1i = self . _context . get ( "is_design" , False )
  if IiiI1i :
   Ii1I11ii1i [ "design" ] = True
   ooOOo00O00Oo = i1Iii11Ii1i1 % ( _ ( u"""请在康虎云报表设计器设计报表。<br/>
            如果报表设计器未打开，请检查康虎云报表是否已启动！<br/><br/><br/>
            模板设计完成后，请在odoo菜单“康虎云报表”--&gt;“模板”菜单中，打开模板记录上传或更新模板！<br/><br/>
            <a href=\"cfprint://open\">启动康虎云报表</a>
            """ ) )
   values . update ( show_message = ooOOo00O00Oo )
   if 42 - 42: O0 / Ooo00oOo00o + OoooooooOO * Oo % Oo
  if I1iiIIIi11 . use_client_templ and I1iiIIIi11 . client_templ_name :
   Ii1I11ii1i [ "template" ] = I1iiIIIi11 . client_templ_name
  else :
   if not I1iiIIIi11 . template_id or not I1iiIIIi11 . template_id . templ_id :
    values . update ( show_message = i1Iii11Ii1i1 % ( _ ( u"未指定要打印的报表模板，请先指定报表模板。" ) ) )
   i1iIi = self . env [ 'cf.template' ] . search ( [ ( 'templ_id' , '=' , I1iiIIIi11 . template_id . templ_id ) ] , limit = 1 ) . template
   if not i1iIi or i1iIi == "" :
    if not IiiI1i :
     values . update ( show_message = i1Iii11Ii1i1 % ( _ ( u"指定的报表模板未定义或模板无内容，请先设计模板并更新到模板记录表。</h3>" ) ) )
    else :
     Ii1I11ii1i [ "template" ] = "cf_templ_%s" % ( I1iiIIIi11 . name . replace ( '.' , '_' ) )
   else :
    Ii1I11ii1i [ "template" ] = "base64:" + i1iIi . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" )
    if 21 - 21: iiiiIi11i / oOoO0oo0OOOo + o0000oOoOoO0o + OoooooooOO
  II1iIi11 = { }
  o0OOOoO0 = values . get ( "docs" )
  if not o0OOOoO0 or len ( o0OOOoO0 ) < 1 :
   OoOo = self . _context . get ( "active_ids" , [ ] )
   o0OOOoO0 = self . env [ I1iiIIIi11 . model_id . model ] . browse ( OoOo )
   if 35 - 35: Oo * II11iiII . OoOO0ooOOoo0O * Ooo00oOo00o . oOo0O0Ooo / O0
  o000oo ( I1iiIIIi11 , I1iiIIIi11 . model_id , I1iiIIIi11 . field_ids , o0OOOoO0 , II1iIi11 )
  if 100 - 100: o0oo0o . Ooo00oOo00o * OoO0O00 % O0 * O0
  if 14 - 14: oOoO0oo0OOOo . Oo + II111iiii / i1I1ii1II1iII / OoOO0ooOOoo0O
  for ooo0O , ( iII1iii , i11i1iiiII ) in enumerate ( II1iIi11 . items ( ) ) :
   ooOO0oO0oo00o = string . capwords ( iII1iii ) . replace ( "." , "_" )
   oOOo0oo0O = i11i1iiiII [ "cols" ]
   IiiIiI1Ii1i = i11i1iiiII [ "rows" ]
   Ii1I11ii1i [ "Tables" ] . append ( {
 "Name" : ooOO0oO0oo00o ,
 "Cols" : oOOo0oo0O ,
 "Data" : IiiIiI1Ii1i ,
 } )
   if 22 - 22: oooO0oo0oOOOO / i11iIiiIii
  return Ii1I11ii1i
  if 62 - 62: ooOO00oOo / oOoO0oo0OOOo
 def _set_report_data ( self , values , report_data ) :
  if 7 - 7: OoooooooOO . oooO0oo0oOOOO
  if 53 - 53: o0000oOoOoO0o % o0000oOoOoO0o * Ooo00oOo00o + oOo0O0Ooo
  if 92 - 92: OoooooooOO + i1IIi / o0000oOoOoO0o * O0
  O00oOo00o0o = [
 "var cfprint_addr = \"127.0.0.1\"" ,
 "var _delay_close = -1"
 ]
  IiII1IiiIiI1 . debug ( 'Dump report data to json...' )
  O00oO0 = json . dumps ( report_data )
  if 70 - 70: OoOO0ooOOoo0O . oOoO0oo0OOOo * OoooooooOO - oooO0oo0oOOOO * oo + oOo0O0Ooo
  if 10 - 10: Ooo00oOo00o / i11iIiiIii
  IiII1IiiIiI1 . debug ( 'Encrypt report data...' )
  i1 = ii1I . rand_aes_key ( 16 , False )
  IiII1IiiIiI1 . debug ( "AES Key: %s" % ( i1 ) )
  o00 = ii1I ( i1 , AES . MODE_CBC )
  oOO00O0Ooooo00 = o00 . encrypt ( O00oO0 ) ;
  if 97 - 97: Oo / o0oo0o % i1IIi % oOoO0oo0OOOo
  if 18 - 18: iIii1I11I1II1 % OoOO0ooOOoo0O
  IiII1IiiIiI1 . debug ( 'Encrypt key...' )
  if 95 - 95: Oo + i11iIiiIii * o0oo0o - i1IIi * o0oo0o - iIii1I11I1II1
  if 75 - 75: OoooooooOO * oooO0oo0oOOOO
  if 9 - 9: oooO0oo0oOOOO - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: oooO0oo0oOOOO * OoO0O00 + iIii1I11I1II1 - oooO0oo0oOOOO + II11iiII
  o00 = ii1I ( OooO0OO ( ) , AES . MODE_CBC )
  o0 = o00 . encrypt ( i1 ) ;
  if 30 - 30: O0 * OoooooooOO
  I1iIIIi1 = {
 "token" : o0 . decode ( "utf-8" ) ,
 "dea" : "aes" ,
  "tea" : "aes" ,
  "data" : oOO00O0Ooooo00 . decode ( "utf-8" )
 }
  if 17 - 17: iIii1I11I1II1 . OoooooooOO / OoOO0ooOOoo0O % II111iiii % i1IIi / i11iIiiIii
  IiII1IiiIiI1 . debug ( 'Dump final_data...' )
  if 58 - 58: OoO0O00 . II111iiii + iiiiIi11i - i11iIiiIii / II111iiii / O0
  O00oOo00o0o . append ( "var _data = %s" % ( json . dumps ( I1iIIIi1 ) ) )
  if 85 - 85: oOo0O0Ooo + II11iiII
  O00oOo00o0o . append ( """_reportData = JSON.stringify(_data);\nconsole.log(_reportData);""" )
  I1II = ";\n" . join ( O00oOo00o0o )
  IiII1IiiIiI1 . debug ( 'json_data: %s ...' % ( I1II [ 0 : 300 ] ) )
  if 27 - 27: II111iiii / o0000oOoOoO0o . II11iiII
  values . update (
 cfprint_json = I1II ,
 )
  if 9 - 9: Oo - oOoO0oo0OOOo - i1I1ii1II1iII
 @ api . multi
 def render ( self , template , values = None ) :
  if values is None :
   if 82 - 82: oooO0oo0oOOOO - oooO0oo0oOOOO + oOo0O0Ooo
   if 8 - 8: Ooo00oOo00o % i1I1ii1II1iII * iiiiIi11i % o0000oOoOoO0o . Oo / Oo
   if 81 - 81: ooOO00oOo
   if 99 - 99: iiiiIi11i * II111iiii * o0oo0o
   if 92 - 92: OoO0O00
   if 40 - 40: oOo0O0Ooo / oooO0oo0oOOOO
   values = { }
   if 79 - 79: ooOO00oOo - iIii1I11I1II1 + o0000oOoOoO0o - o0oo0o
  IiII1IiiIiI1 . debug ( "Render report..." )
  iiIiI1i1 = self . _get_report_from_name ( template )
  if not iiIiI1i1 :
   raise AccessError ( _ ( u"未找到报表（%s）定义，可能是报表未定义或定义未生效，如果使用康虎云报表，请在报表定义中重新生成一下报表定义！" % ( template ) ) )
   if 93 - 93: II111iiii . oo - OoO0O00 + oOo0O0Ooo
  ooOOo00O00Oo = i1Iii11Ii1i1 % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
  if 61 - 61: II111iiii
  IiII1IiiIiI1 . debug ( "Prepare docs..." )
  o0OOOoO0 = values . get ( "docs" , False )
  if not o0OOOoO0 or len ( o0OOOoO0 ) < 1 :
   OoOo = self . _context . get ( "active_ids" , [ ] )
   o0OOOoO0 = self . env [ iiIiI1i1 . model ] . browse ( OoOo )
   values . update ( docs = o0OOOoO0 )
  if not o0OOOoO0 or len ( o0OOOoO0 ) < 1 :
   ooOOo00O00Oo = i1Iii11Ii1i1 % ( _ ( u"没有可以打印数据。" ) )
   if 15 - 15: i11iIiiIii % oo * OoOO0ooOOoo0O / o0oo0o
  IiII1IiiIiI1 . debug ( "Retrieve report define..." )
  if 90 - 90: i1I1ii1II1iII
  i1i1i1I = iiIiI1i1 . xml_id . split ( "." )
  if len ( i1i1i1I ) > 1 :
   i1i1i1I = i1i1i1I [ 1 ] . replace ( II1I , "" )
  else :
   i1i1i1I = i1i1i1I [ 0 ] . replace ( II1I , "" )
   if 83 - 83: iiiiIi11i + OoooooooOO
  values . update (
 show_message = ooOOo00O00Oo
 )
  if 22 - 22: o0000oOoOoO0o % i1I1ii1II1iII * OoooooooOO - Ooo00oOo00o / iIii1I11I1II1
  if 86 - 86: OoooooooOO . i1I1ii1II1iII % oOo0O0Ooo / OoOO0ooOOoo0O * i1I1ii1II1iII / Ooo00oOo00o
  oOoOOo000oOoO0 = self . env [ "cf.report.define" ] . search ( [ ( 'name' , '=' , i1i1i1I ) ] , limit = 1 )
  if 86 - 86: II111iiii % i11iIiiIii + o0000oOoOoO0o % i11iIiiIii
  IiII1IiiIiI1 . debug ( "Prepare to make json...[%s]" % ( i1i1i1I ) )
  if oOoOOo000oOoO0 :
   IiII1IiiIiI1 . debug ( "Set report_define to values..." )
   values . update ( report_define = oOoOOo000oOoO0 , )
   IiII1IiiIiI1 . debug ( "Begin to make report data ..." )
   Ooo0o0OOO = self . _make_cfprint_json ( values )
   IiII1IiiIiI1 . debug ( "Begin to convert report data to json..." )
   self . _set_report_data ( values , Ooo0o0OOO )
   IiII1IiiIiI1 . debug ( "Converted!!!" )
   if 35 - 35: II11iiII + i1I1ii1II1iII
  OOO0O00oO = super ( OoO0O00O0oo0O , self ) . render ( template , values )
  return OOO0O00oO
  if 40 - 40: Ooo00oOo00o
 def action_upload_templ_win ( self ) :
  OOOooo = self . _context . get ( "templ_id" , False )
  return {
 'name' : _ ( u'上传康虎云报表模板' ) ,
 'type' : 'ir.actions.act_window' ,
 'view_type' : 'form' ,
 'res_model' : 'cf.template' ,
 'res_id' : OOOooo ,

  'context' : self . _context ,
 'target' : 'current' ,
 'nodestroy' : True
 }
  if 99 - 99: II111iiii * oooO0oo0oOOOO % iIii1I11I1II1 / o0000oOoOoO0o
 @ api . model
 def render_qweb_html ( self , docids , data = None ) :
  if not docids :
   docids = data . get ( "docids" , None )
   if 90 - 90: iiiiIi11i % II11iiII - II11iiII % II111iiii * ooOO00oOo
  iIi1iI111I = data . get ( "is_design" , False )
  Ooooo00o0OoO = _ ( u"设计" ) if iIi1iI111I else _ ( u"打印" )
  oOoOOo000oOoO0 = self . cf_report_define_id
  if 75 - 75: oo % II111iiii
  ooOOo00O00Oo = i1Iii11Ii1i1 % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
  if 30 - 30: oooO0oo0oOOOO + o0oo0o - oooO0oo0oOOOO . oooO0oo0oOOOO - II111iiii + O0
  o0OOOoO0 = data . get ( "docs" , False )
  if 86 - 86: i1IIi
  if ( not o0OOOoO0 or not isinstance ( o0OOOoO0 , list ) or len ( o0OOOoO0 ) < 1 ) and docids :
   o0OOOoO0 = self . env [ oOoOOo000oOoO0 . model_id . model ] . browse ( docids )
   if 41 - 41: oOo0O0Ooo * OoOO0ooOOoo0O / oOo0O0Ooo % iiiiIi11i
  if not o0OOOoO0 or len ( o0OOOoO0 ) < 1 :
   ooOOo00O00Oo = i1Iii11Ii1i1 % ( _ ( u"没有可以%s数据。" ) % ( Ooooo00o0OoO ) )
   if 18 - 18: II111iiii . OoooooooOO % oOo0O0Ooo % o0000oOoOoO0o
  data . update ( docs = o0OOOoO0 , show_message = ooOOo00O00Oo , )
  if 9 - 9: ooOO00oOo - OoO0O00 * OoooooooOO . OoO0O00
  if oOoOOo000oOoO0 :
   data . update ( report_define = oOoOOo000oOoO0 , )
   Ooo0o0OOO = self . with_context ( is_design = iIi1iI111I ) . _make_cfprint_json ( data )
   self . _set_report_data ( data , Ooo0o0OOO )
   if 2 - 2: OoooooooOO % II11iiII
  return super ( OoO0O00O0oo0O , self ) . render_qweb_html ( docids , data )
  if 63 - 63: oo % iIii1I11I1II1
  if 39 - 39: i1I1ii1II1iII / II111iiii / oOoO0oo0OOOo % oo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
