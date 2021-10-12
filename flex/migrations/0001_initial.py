# Generated by Django 3.2.7 on 2021-10-10 18:41

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='Add Additional Text', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', streams.blocks.SimpleRichtextBlock(features=['bold', 'italic'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=True))]))], blank=True, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('body', wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=50))])), ('list', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(), label='Items'))])), ('image_text_overlay', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))])), ('cropped_images_with_text', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))]), label='Image Item'))])), ('list_with_images', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=200, required=False)), ('link_url', wagtail.core.blocks.URLBlock(label='Link URL', max_length=200, required=False))]), label='List Item'))])), ('thumbnail_gallery', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]), label='Image'))])), ('chart', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Chart Title', label='Title', max_length=120)), ('chart_type', wagtail.core.blocks.ChoiceBlock(choices=[('bar', 'Bar'), ('horizontalBar', 'Horizontal Bar'), ('pie', 'Pie'), ('doughnut', 'Doughnut'), ('polarArea', 'Polar Area'), ('radar', 'Radar'), ('line', 'Line')], label='Chart Type')), ('labels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(default='Label', label='Label', max_length=40), label='Chart Labels')), ('datasets', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(default='Dataset #1', label='Dataset Label', max_length=120)), ('dataset_data', wagtail.core.blocks.ListBlock(wagtail.core.blocks.IntegerBlock(), default='0', label='Data'))]), label='Dataset'))])), ('map', wagtail.core.blocks.StructBlock([('marker_title', wagtail.core.blocks.CharBlock(default="Marker Title 'This will be updated after you save changes.'", max_length=120)), ('marker_description', wagtail.core.blocks.RichTextBlock()), ('zoom_level', wagtail.core.blocks.IntegerBlock(default='2', max_value=18, min_value=0, required=False)), ('location_x', wagtail.core.blocks.FloatBlock(default='35.0', required=False)), ('location_y', wagtail.core.blocks.FloatBlock(default='0.16', required=False)), ('marker_x', wagtail.core.blocks.FloatBlock(default='51.5', required=False)), ('marker_y', wagtail.core.blocks.FloatBlock(default='-0.09', required=False))])), ('image_slider', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]), label='Image'))]))], blank=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('thank_you_text', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Flex Page',
                'verbose_name_plural': 'Flex Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_form_fields', to='flex.flexpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
