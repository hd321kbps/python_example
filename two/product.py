#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mInvoice
import mDocument
import argparse
import sqlite3
import logging
import logging.handlers

if __name__ == "__main__":

	# Открыть документацию питон (python -m pydoc -b)

	# Doc = mDocument.Document()
	# Doc.create_table()

	# @classmethod
	AP = argparse.ArgumentParser(description='Process some integers.')
	AP.add_argument('-i', '--initdb', dest='initdb', action='store_true', default=False, help='Initialise database')
	args = AP.parse_args()

	LOG = logging.getLogger("main")
	LOG.setLevel(logging.DEBUG)
	
	handler = logging.handlers.RotatingFileHandler("product.log", maxBytes=20*1024, backupCount=5)
	fmt = logging.Formatter("%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s")
	handler.setFormatter(fmt)

	LOG.addHandler(handler)

	LOG.debug("Program started")

	if args.initdb:
		try:
			mInvoice.Invoice.create_table()
		except sqlite3.DatabaseError as Exc:
			print(Exc.args)

	else:
		try:
		# 	with mInvoice.Invoice(id = 1) as Doc:
		# 		print(Doc.id, Doc._status, len(Doc))
		# 		print(Doc)
			Inv = mInvoice.create()
			Inv.append_blank(title="Каранадаш", unit="шт")
			Inv.append_blank()
			print(Inv)
			print(str(Inv))
			print("Всего позиций в накладной: ", len(Inv))
			Inv.save()
			# Doc = mInvoice.Invoice(id=14)
			# Doc.restore()
			# print(Doc.id, Doc._status, len(Doc))

			# print(x)
			# print(200/0)
			# Doc = mDocument.load(id=5)
			# Не работает
			# Doc = mInvoice.Invoice(status=mDocument.Document.New)
			# Doc.save()
			# Doc = mInvoice.Invoice(id=9)
			# Doc.restore()
			# Doc = mDocument.create()
			# Doc.save()
			# print(Doc.id, Doc._status, Doc._total)
		except mDocument.NotFound:
			print("Документ не найден")
		except mDocument.Error:
			print("Какая-то ошибка при работе с документом")
		# except sqlite3.DatabaseError:
		# 	print("Какая-то ошибка при работе с базой данных")
		except NameError:
			print("Какая-то неизвестная штука")
		except ZeroDivisionError:
			print("Делить на 0 нельзя")
		# Все остальные
		# except Exception:
		# 	print("Где-то что-то не то")
		# Invoice = mInvoice.create()
		# Invoice.append_blank()
		# # Invoice.get_position(0).set_title("Карандаши")
		# # __str__
		# # Invoice.get_position(0).title = "Карандаши"
		# # Invoice.get_position(0).unit = "шт"
		# # __getitem__
		# Invoice[0].title = "Карандаши"
		# Invoice[0].unit = "шт"

		# Invoice.append_blank()

		# print(Invoice)
		# # print(Invoice.dump())
		# print("Всего позици в накладной:", len(Invoice))