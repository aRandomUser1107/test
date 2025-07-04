# Generated by Django 5.1.7 on 2025-04-25 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                ("""
                    CREATE TABLE blog_post (
                        id serial primary key,
                        title varchar(255) NOT NULL,
                        content text NOT NULL,
                        created_at date default now()
                    );
                """)
            ], 

            reverse_sql=[
                ("""
                    drop table if exists blog_post;
                """)
            ])
    ]

