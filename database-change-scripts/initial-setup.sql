create table snowshoveler_schema_version
(
    script_path citext primary key,
    script_contents text,
    inserted timestamp not null default now(),
    updated timestamp
);

create or replace function set_updated_column ()
returns trigger
as
$$

begin

    NEW.updated = now();
    return NEW;

end;
$$
language plpgsql;

create trigger snowshoveler_schema_version_set_updated_column
before update
on snowshoveler_schema_version
for each row
execute procedure set_updated_column();
