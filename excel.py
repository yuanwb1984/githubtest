# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:04:34 2016

@author: 06210
"""

import win32com
import win32api
import win32con

win32api.MessageBox(win32con.NULL,'asd','sad',win32con.MB_OK)

   
excel2 = win32com.client.gencache.EnsureDispatch('Excel.Application')
excel2.Visible = True
wb = excel2.Workbooks.Open(r'C:\Users\06210\Desktop\袁文彬\githubtest\Book1.xlsx')
wb.Close()
excel2.Quit()
