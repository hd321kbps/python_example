#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mDocument
import mInvoicePos
import sqlite3
import logging

def create():
	return Invoice(status = mDocument.Document.New)

# Класс утилит - класс в котором только статические методы
# Абстрактный класс - класс который не имеет экземпляров класса
# Интерфейс - набор методов которые обязательно долны быть в классах использующих этот интерфейс
# Примеси в Ruby это интерфейс с одним методом без конструктора
# Мета класс - это такой класс экземпляром, которого являеться класс
# Функтор - это объект, который можно вызывать, как функцию
class Invoice(mDocument.Document):
	def __init__(self, **kwargs):
		if "total" in kwargs:
			self.__Total = kwargs["total"]
			del kwargs["total"]
		# mDocument.Document.__init__(self, **kwargs)
		# proxy объект
		super(Invoice, self).__init__(**kwargs)
		self.__Positions = []

	def __enter__(self):
		self.restore()

	def __exit__(self, exc_type, exc_value, traceback):
		self.save()

	total = property(lambda self: self.__Total)

	# @property
	# def _total(self):
	# 	try:
	# 		return self.total
	# 	except AttributeError:
	# 		return None
	
	@classmethod
	def create_table(self):
		try:
			mDocument.Document.create_table()
		except sqlite3.OperationalError:
			pass
		# conn = sqlite3.connect(os.path.expanduser("~/data.db"))
		# conn = sqlite3.connect("data.db")
		path = "data.db"
		with sqlite3.connect(path) as conn:
			curr = conn.cursor()
			curr.execute('''
				create table t_invoice(
					r_id_document integer not null primary key references t_document(i_id),
					f_total numeric(22, 2) null
				)
			''')
			conn.commit()
			conn.close()
			mInvoicePos.InvoicePos.create_table()

	def __len__(self):
		return len(self.__Positions)

	# def get_position(self, index):
	def __getitem__(self, index):
		return self.__Positions[index]

	def __iter__(self):
		for P in self.__Positions:
			yield P

	def append_blank(self, **kwargs):
		self.__Positions.append(mInvoicePos.InvoicePos(self, **kwargs))

	def append(self, position):
		if not isinstance(position, mInvoicePos.InvoicePos):
			raise ValueError
		self.__Positions.append(position)

	def delete(self, index):
		del self.__Positions[index]

	# def save(self):
	# 	# Staticmethod
	# 	with self.connect() as conn:
	# 		curr = conn.cursor()
	# 		try:
	# 			curr.execute('''
	# 				update t_document
	# 					set f_status = ?
	# 					where i_id = ?
	# 			''', (self._status, self.id))
	# 		except AttributeError:
	# 			curr.execute("insert into t_document(f_status) values (?)", (self._status,))

	# 			curr.execute("select max(i_id) from t_document")

	# 			for(id) in curr:
	# 				self.__Id = id

	def save(self):
		with self.connect() as conn:
			self._save(conn)
			curr = conn.cursor()
			# тут ошибка
			curr.execute("update t_document set f_kind = ? where i_id = ?", (1, self.id))
			try:
				curr.execute("insert into t_invoice(r_id_document, f_total) values (?, ?)", (self.id, self._total))
			except sqlite3.IntegrityError:
				curr.execute("update t_invoice set f_total = ? where r_id_document = ?", (self._total, self.id))

			for P in self:
				P.save(conn)

	def restore(self):
		with self.connect() as conn:
			curr = conn.cursor()
			curr.execute("select doc.f_status, inv.f_total from t_document doc inner join t_invoice inv on doc.i_id = inv.r_id_document where i_id = ?", (self.id,))

			for (status, total) in curr:
				self.Document__Status = status
				if self.Document__Status == None:
					del self.Document__Status
				self.__Total = total
				if self.__Total == None:
					del self.__Total
				break
			else:
				raise mDocument.NotFound()
			
			self.__Positions = []
			curr.execute("select i_id, f_title, f_unit, f_amount, f_price, f_sum from t_position where r_id_invoice = ? order by f_order", (self.id,))

			for (id, title, unit, amount, price, sum) in curr:
				self.append_blank(id=id, titile=title, amount=amount, price=price, sum=sum)

		logging.getLogger('main').info("Document ID=%d restored" % self.id)

	# Вызывается при преобразование в юникод
	# def __unicode__(self):
	# 	pass

	# Вызывается при вызове print
	# def __repr__(self):
	# 	pass

	# def dump(self):
	# Вызывается при преобразование в строку
	def __str__(self):
		Pos = ""
		K = 1
		# for P in self.__Positions:
		# __iter__
		for P in self:
			Pos += "%s. %s\n" % (K, P)
			K += 1

		Result = "(ID: %s) (Status: %s)\n" % (self._id, self._status)
		Result += "Накладная\n"
		Result += "%s" % (Pos)
		Result += "Итого: %s" % (self._total)

		# Result = '''
		# 	(ID: %s) (Status: %s)
		# 	Накладная
		# 	%s
		# 	Итого: %s
		# 	''' % \
		# 	(self._id, self._status, Pos, self._total)
		
		return Result

if __name__ == "__main__":
	Inv = create()

	try:
		print("Status = ", Inv.status)
	except AttributeError:
		print("<NONE>")
	try:
		print("ID =  ", Inv.id)
	except AttributeError:
		print("<NONE>")