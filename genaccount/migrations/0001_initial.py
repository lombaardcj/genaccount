# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True, unique=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Equity'), (4, 'Income'), (5, 'Cost of Sales'), (6, 'Expense'), (7, 'Other Income'), (8, 'Other Expense')], blank=True)),
                ('comment', models.CharField(max_length=50, null=True, blank=True)),
                ('balance', models.DecimalField(default='0.00', decimal_places=2, max_digits=10)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasicJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('postdate', models.DateTimeField(default=django.utils.timezone.now, help_text='When Journal was posted')),
                ('comment', models.CharField(help_text='Short comment on journal action', max_length=50, db_index=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descr', models.CharField(help_text='Description of the journal transaction entry', max_length=50, blank=True, db_index=True)),
                ('balance', models.DecimalField(default='0.00', decimal_places=2, help_text='Postive balance always debit, negative balance always credit', max_digits=10)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genaccount.Account')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('basic_journal', models.ForeignKey(to='genaccount.BasicJournal')),
            ],
        ),
    ]
