# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(db_index=True, unique=True, max_length=50)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Asset'), (2, 'Liability'), (3, 'Equity'), (4, 'Income'), (5, 'Cost of Sales'), (6, 'Expense'), (7, 'Other Income'), (8, 'Other Expense')], blank=True)),
                ('comment', models.CharField(null=True, max_length=50, blank=True)),
                ('balance', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasicJournal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('postdate', models.DateTimeField(help_text='When Journal was posted', default=django.utils.timezone.now)),
                ('comment', models.CharField(db_index=True, max_length=50, help_text='Short comment on journal action')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descr', models.CharField(db_index=True, max_length=50, blank=True, help_text='Description of the journal transaction entry')),
                ('balance', models.DecimalField(decimal_places=2, help_text='Postive balance always debit, negative balance always credit', default='0.00', max_digits=10)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genaccount.Account')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('basic_journal', models.ForeignKey(blank=True, to='genaccount.BasicJournal', null=True)),
            ],
        ),
    ]
