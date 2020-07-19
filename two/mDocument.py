#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
# import os.path

# Создание своего исключения
class Error(Exception):
	pass
class NotFound(Error):
	pass

def create():
	'''Create new Document'''
	return Document(status = Document.New)

def load(id):
	'''Load document from database'''
	Doc = Document(id = id)
	Doc.restore()
	return Doc

class Document(object):
	New = 1
	Status_Allowed = [New]

	def __init__(self, **kwargs):
		if "id" in kwargs:
			self.__Id = kwargs["id"]
			del kwargs["id"]
		if "status" in kwargs:
			if kwargs["status"] not in Document.Status_Allowed:
				raise ValueError
			self.__Status = kwargs["status"]
			del kwargs["status"]
		self.__Others = {}
		for (keys, value) in kwargs.items():
			self.__Others[keys] = value
	
	def __getattribute__(self, name):
		if name[0] != "_":
			return super(Document, self).__getattribute__(name)
		if "__" in name:
			return super(Document, self).__getattribute__(name)
		if name in self.__dict__:
			return super(Document, self).__getattribute__(name)
		if name in type(self).__dict__:
			return super(Document, self).__getattribute__(name)

		for base in type(self).__bases__:
			if name in base.__dict__:
				return super(Document, self).__getattribute__(name)

		Name = name[1:]
		try:
			return super(Document, self).__getattribute__(Name)
		except AttributeError as Exc:
			if ("'%s'" % Name) in str(Exc):
				raise
			return None

	id = property(lambda self: self.__Id)
	status = property(lambda self: self.__Status)

	# Два подчекивания метод класса
	# Одно подчеркивания метод класса виден в наследующих клаcсах
	
	# @property
	# def _id(self):
	# 	try:
	# 		return self.id
	# 	except AttributeError:
	# 		return None

	# @property
	# def status(self):
	# 	return self.__Status

	# @status.setter
	# def status(self, value):
	# 	self.__Status = value
	# 	if self.__Status == None:
	# 		del self.__Status

	# @property
	# def _status(self):
	# 	try:
	# 		return self.status
	# 	except AttributeError:
	# 		return None

	@staticmethod
	# def connect(self):
	def connect():
		# conn = sqlite3.connect(os.path.expanduser("~/data.db"))
		path = "data.db"
		return sqlite3.connect(path)

	def _save(self, conn):
			curr = conn.cursor()
			try:
				curr.execute('''
					update t_document
						set f_status = ?
						where i_id = ?
				''', (self._status, self.id))
			except AttributeError:
				curr.execute("insert into t_document(f_status) values (?)", (self._status,))

				curr.execute("select max(i_id) from t_document")

				for(id) in curr:
					self.__Id = id

	def save(self):
		with Document.connect() as conn:
			self._save(conn)

	def restore(self):
		with Document.connect() as conn:
			curr = conn.cursor()
			curr.execute("select f_status from t_document where i_id = ?", (self.id,))

			for (status,) in curr:
				self.__Status = status
				if self.__Status == None:
					del self.__Status
				return
			raise NotFound()
	
	# @staticmethod
	# def create_table(self):
	@classmethod
	def create_table(self):
		with Document.connect() as conn:
			curr = conn.cursor()
			curr.execute('''
				create table t_document(
					i_id integer not null primary key autoincrement,
					f_status integer null,
					f_kind integer null
				);
			''')

if __name__ == "__main__":
	Doc = create()
	print("Status ", Doc.status)
	try:
		print("ID =  ", Doc.id)
	except AttributeError:
		print("<NONE>")

	Doc = load(id = 1)
	try:
		print("Status = ", Doc.status)
	except AttributeError:
		print("<NONE>")
	try:
		print("ID =  ", Doc.id)
	except AttributeError:
		print("<NONE>")

	Doc = load(id = "123")
	try:
		print("Status = ", Doc.status)
	except AttributeError:
		print("<NONE>")
	try:
		print("ID =  ", Doc.id)
	except AttributeError:
		print("<NONE>")