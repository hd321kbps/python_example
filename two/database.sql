create table t_document(
	i_id integer not null primary key autoincrement,
	f_status integer null,
	f_kind integer null
);
create table t_invoice(
	r_id_document integer not null primary key references t_document(i_id),
	f_total numeric(22, 2) null
);
create table t_position(
	i_id integer not null primary key autoincrement,
	r_id_invoice integer nor null references t_invoice(i_id),
	f_order integer not null,
	f_title text null,
	f_unit text null,
	f_amount integer null,
	f_price numeric(22, 4) null,
	f_sum numeric(22, 2) null
);