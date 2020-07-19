#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import weakref
import decimal

class Field(object):
	def __init__(self, field_type, is_pk = False, is_nullable = True, db_type = None):
		self.__Type = field_type
		if db_type != None: self.__DbType = db_type
		self.__IsPk = is_pk
		self.__IsNullable = is_nullable

	field_type = property(lambda self: self.__Type)
	is_nullable = property(lambda self: self.__IsNullable or self.is_pk)
	is_pk = property(lambda self: self.__IsPk)

	@property
	def db_type(self):
		try:
			return self.__DbType
		except AttributeError:
			if self.field_type in [int]:
				return "integer"
			if self.field_type in [str]:
				return "text"
			raise

	def sql(self):
		Result = self.db_type
		Result += " NULL" if self.is_nullable else " NOT NULL"
		if self.is_pk:
			Result += " primary key autoincrement"
		return Result

class DecimalField(Field):
	def __init__(self, width = 22, prec = 2, is_nullable = True):
		super(DecimalField, self).__init__(field_type = decimal.Decimal, is_nullable = is_nullable)
		self.__Width = width
		self.__Prec = prec

	width = property(lambda self: self.__Width)
	prec = property(lambda self: self.__Prec)

	@property
	def db_type(self):
		return "numeric(%d, %d)" % (self.width, self.prec)

class InvoicePos(object):

	Id = Field(int, is_pk = True)
	IdInvoice = Field(int, is_nullable = False)
	Order = Field(int, is_nullable = False)
	Title = Field(str)
	Unit = Field(str)
	Amount = Field(int)
	Price = DecimalField(22, 4)
	Sum = DecimalField(22, 2)


	def __init__(self, parent, **kwargs):
		self.__Parent = weakref.proxy(parent)

		if "id" in kwargs: self.__Id = kwargs["id"]
		if "title" in kwargs: self.__Title = kwargs["title"]
		if "unit" in kwargs: self.__Unit = kwargs["unit"]
		if "amount" in kwargs: self.__Amount = kwargs["amount"]
		if "price" in kwargs: self.__Price = kwargs["price"]
		if "sum" in kwargs: self.__Sum = kwargs["sum"]
	
	id = property(lambda self: self.__Id)
	parent = property(lambda self: self.__Parent)
	# Сохращенная запись
	# title = property(lambda self: self.__Title)
	# unit = property(lambda self: self.__Unit)
	# price = property(lambda self: self.__Price)
	# amount = property(lambda self: self.__Amount)
	# sum = property(lambda self: self.__Sum)

	@property
	def order(self):
		for K in range(0, len(self.parent)):
			if self is self.parent[K]:
				return K
			raise IndexError

	# Старый способ
	def get_title(self):
		return self.__Title

	def set_title(self, title):
		self.__Title = title

	def del_title(self):
		del self.__Title

	title = property(get_title, set_title, del_title)

	@property
	def _id(self):
		try:
			return self.id
		except AttributeError:
			return None
	
	@property
	def _title(self):
		try:
			return self.title
		except AttributeError:
			return None

	@property
	def _unit(self):
		try:
			return self.unit
		except AttributeError:
			return None
	
	@property
	def _price(self):
		try:
			return self.price
		except AttributeError:
			return None

	@property
	def _amount(self):
		try:
			return self.amount
		except AttributeError:
			return None

	@property
	def _sum(self):
		try:
			return self.sum
		except AttributeError:
			return None

	@classmethod
	def sql(self):
		FSql = []
		for (name, attr) in self.__dict__.items():
			if isinstance(attr, Field):
				FSql.append("f_" + name + " " + attr.sql())
		return "create_table t_%s ( \n%s \n);" % (self.__name__, ", \n".join(FSql))

	@classmethod
	def create_table(self):
		# conn = sqlite3.connect(os.path.expanduser("~/data.db"))
		path = "data.db"
		with sqlite3.connect(path) as conn:
			curr = conn.cursor()
			curr.execute('''
				create table t_position(
					i_id integer not null primary key autoincrement,
					f_id_invoice integer nor null references t_invoice(i_id),
					f_order integer not null,
					f_title text null,
					f_unit text null,
					f_amount integer null,
					f_price numeric(22, 4) null,
					f_sum numeric(22, 2) null
				);
			''')

	# Новый способ
	@property
	def unit(self):
		return self.__Unit

	@unit.setter
	def unit(self, unit):
		self.__Unit = unit

	@unit.deleter
	def unit(self):
		del self.__Unit

	@property
	def price(self):
		return self.__Price

	@price.setter
	def price(self, price):
		self.__Price = price

	@price.deleter
	def price(self):
		del self.__Price

	@property
	def amount(self):
		return self._Amount

	@amount.setter
	def amount(self, amount):
		self._Amount = amount

	@amount.deleter
	def amount(self):
		del self._Amount

	@property
	def sum(self):
		try:
			return self.__Sum
		except AttributeError:
			return self.amount * self.price

	@sum.setter
	def sum(self, sum):
		self.__Sum = sum

	@sum.deleter
	def sum(self):
		del self.__Sum

	def save(self, conn):
		curr = conn.cursor()
		try:
			curr.execute("update t_position set f_order = ?, f_title = ?, f_unit = ?, f_amount = ?, f_price = ?, f_sum = ? where i_id = ?", (self.order, self._title, self._unit, self._amount, self._price, self._sum, self.id))
		except AttributeError:
			curr.execute("insert into t_position(r_id_document, f_order, f_title, f_unit, f_amount, f_price, f_sum) values (?, ?, ?, ?, ?, ?, ?)", (self.parent.id, self.order, self._title, self._unit, self._amount, self._price, self._sum))
		
		curr.execute("select max(i_id) from t_position")
		for (id,) in curr:
			self.__Id = id

	def __str__(self):
		return "%s, %s, %s, %s, %s, %s" % (
			self._id,
			self._title,
			self._unit,
			self._price,
			self._amount,
			self._sum
		)