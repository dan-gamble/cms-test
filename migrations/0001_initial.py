# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20140909_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_online', models.BooleanField(default=True, help_text=b"Uncheck this box to remove the page from the public website. Logged-in admin users will still be able to view this page by clicking the 'view on site' button.", verbose_name=b'online')),
                ('browser_title', models.CharField(help_text=b"The heading to use in the user's web browser. Leave blank to use the page title. Search engines pay particular attention to this attribute.", max_length=1000, blank=True)),
                ('meta_keywords', models.CharField(help_text=b'A comma-separated list of keywords for this page. Use this to specify common mis-spellings or alternative versions of important words in this page.', max_length=1000, verbose_name=b'keywords', blank=True)),
                ('meta_description', models.TextField(help_text=b'A brief description of the contents of this page.', verbose_name=b'description', blank=True)),
                ('sitemap_priority', models.FloatField(default=None, choices=[(1.0, b'Very high'), (0.8, b'High'), (0.5, b'Medium'), (0.3, b'Low'), (0.0, b'Very low')], blank=True, help_text=b'The relative importance of this content in your site.  Search engines use this as a hint when ranking the pages within your site.', null=True, verbose_name=b'priority')),
                ('sitemap_changefreq', models.IntegerField(default=None, choices=[(1, b'Always'), (2, b'Hourly'), (3, b'Daily'), (4, b'Weekly'), (5, b'Monthly'), (6, b'Yearly'), (7, b'Never')], blank=True, help_text=b'How frequently you expect this content to be updated.Search engines use this as a hint when scanning your site for updates.', null=True, verbose_name=b'change frequency')),
                ('robots_index', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from indexing this page. Disable this only if the page contains information which you do not wish to show up in search results.', verbose_name=b'allow indexing')),
                ('robots_follow', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from following any links they find in this page. Disable this only if the page contains links to other sites that you do not wish to publicise.', verbose_name=b'follow links')),
                ('robots_archive', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from archiving this page. Disable this only if the page is likely to change on a very regular basis. ', verbose_name=b'allow archiving')),
                ('url_title', models.SlugField(verbose_name=b'URL title')),
                ('title', models.CharField(max_length=1000)),
                ('short_title', models.CharField(help_text=b'A shorter version of the title that will be used in site navigation. Leave blank to use the full-length title.', max_length=200, blank=True)),
                ('content_primary', cms.models.fields.HtmlField(verbose_name=b'primary content', blank=True)),
            ],
            options={
                'verbose_name': 'catgeory',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_online', models.BooleanField(default=True, help_text=b"Uncheck this box to remove the page from the public website. Logged-in admin users will still be able to view this page by clicking the 'view on site' button.", verbose_name=b'online')),
                ('browser_title', models.CharField(help_text=b"The heading to use in the user's web browser. Leave blank to use the page title. Search engines pay particular attention to this attribute.", max_length=1000, blank=True)),
                ('meta_keywords', models.CharField(help_text=b'A comma-separated list of keywords for this page. Use this to specify common mis-spellings or alternative versions of important words in this page.', max_length=1000, verbose_name=b'keywords', blank=True)),
                ('meta_description', models.TextField(help_text=b'A brief description of the contents of this page.', verbose_name=b'description', blank=True)),
                ('sitemap_priority', models.FloatField(default=None, choices=[(1.0, b'Very high'), (0.8, b'High'), (0.5, b'Medium'), (0.3, b'Low'), (0.0, b'Very low')], blank=True, help_text=b'The relative importance of this content in your site.  Search engines use this as a hint when ranking the pages within your site.', null=True, verbose_name=b'priority')),
                ('sitemap_changefreq', models.IntegerField(default=None, choices=[(1, b'Always'), (2, b'Hourly'), (3, b'Daily'), (4, b'Weekly'), (5, b'Monthly'), (6, b'Yearly'), (7, b'Never')], blank=True, help_text=b'How frequently you expect this content to be updated.Search engines use this as a hint when scanning your site for updates.', null=True, verbose_name=b'change frequency')),
                ('robots_index', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from indexing this page. Disable this only if the page contains information which you do not wish to show up in search results.', verbose_name=b'allow indexing')),
                ('robots_follow', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from following any links they find in this page. Disable this only if the page contains links to other sites that you do not wish to publicise.', verbose_name=b'follow links')),
                ('robots_archive', models.BooleanField(default=True, help_text=b'Use this to prevent search engines from archiving this page. Disable this only if the page is likely to change on a very regular basis. ', verbose_name=b'allow archiving')),
                ('question', models.CharField(max_length=256)),
                ('answer', cms.models.fields.HtmlField()),
                ('url_title', models.CharField(unique=True, max_length=256)),
                ('order', models.PositiveIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='faqs.Category', null=True, blank=True)),
            ],
            options={
                'ordering': ['order', 'id', 'question'],
                'verbose_name': 'faq',
                'verbose_name_plural': 'faqs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('page', models.OneToOneField(related_name=b'+', primary_key=True, serialize=False, editable=False, to='pages.Page')),
                ('header_text', cms.models.fields.HtmlField(null=True, blank=True)),
                ('footer_text', cms.models.fields.HtmlField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='faq',
            name='page',
            field=models.ForeignKey(to='faqs.Faqs'),
            preserve_default=True,
        ),
    ]
