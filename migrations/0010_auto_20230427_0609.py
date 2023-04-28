# Generated by Django 3.1.3 on 2023-04-27 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esteem', '0009_optionexteriormillworkdeckingcolor_sample_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estirequest',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='optiondoorexteriorcolor',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='optionexteriormillworkdeckingcolor',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='optionmarvindoorexteriorcolor',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='optionwindowexteriorcolor',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='estirequestdocument',
            name='estirequest',
            field=models.ForeignKey(help_text='What is the request to which this document is attached?', on_delete=django.db.models.deletion.CASCADE, to='esteem.estirequest'),
        ),
        migrations.AlterField(
            model_name='estisheetdoor',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand of these doors?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='estisheetexteriormillwork',
            name='deckingcolor',
            field=models.ForeignKey(blank=True, help_text='What is the decking color?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkdeckingcolor'),
        ),
        migrations.AlterField(
            model_name='estisheetexteriormillwork',
            name='deckinggrooves',
            field=models.ForeignKey(blank=True, help_text='What kind of grooving does this decking have?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkdeckinggrooves'),
        ),
        migrations.AlterField(
            model_name='estisheetexteriormillwork',
            name='optionexteriormillworkdeckingbrand',
            field=models.ForeignKey(blank=True, help_text='What is the decking material?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkdeckingbrand'),
        ),
        migrations.AlterField(
            model_name='estisheetexteriormillwork',
            name='optionexteriormillworkdeckingcollection',
            field=models.ForeignKey(blank=True, help_text='What is the decking collection?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkdeckingcollection'),
        ),
        migrations.AlterField(
            model_name='estisheetexteriormillwork',
            name='railingstyle',
            field=models.ForeignKey(blank=True, help_text='What is the railing style?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkrailingstyle'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='primaryspecies',
            field=models.ForeignKey(blank=True, help_text='What is the primary species for this millwork?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optioninteriormillworkprimaryspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair1riserspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this riser?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair1riser', to='esteem.optioninteriormillworkriserspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair1treadspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this tread?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair1tread', to='esteem.optioninteriormillworktreadspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair2riserspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this riser?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair2riser', to='esteem.optioninteriormillworkriserspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair2treadspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this tread?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair2tread', to='esteem.optioninteriormillworktreadspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair3riserspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this riser?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair3riser', to='esteem.optioninteriormillworkriserspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetinteriormillwork',
            name='stair3treadspecies',
            field=models.ForeignKey(blank=True, help_text='What is the species for this tread?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stair3tread', to='esteem.optioninteriormillworktreadspecies'),
        ),
        migrations.AlterField(
            model_name='estisheetmarvindoor',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand of these doors?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='estisheetwindow',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand of these windows?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorexteriorcolor',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorhardwarefinish',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorinteriorfinish',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorlocksensor',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorscreen',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optiondoorshade',
            name='optiondoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optiondoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionexteriormillworkdeckingcollection',
            name='optionexteriormillworkdeckingbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionexteriormillworkdeckingbrand'),
        ),
        migrations.AlterField(
            model_name='optionexteriormillworkdeckingcolor',
            name='optionexteriormillworkdeckingcollection',
            field=models.ForeignKey(blank=True, help_text='What is the decking collection for which this color is an option?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='esteem.optionexteriormillworkdeckingcollection'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorexteriorcolor',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorhardwarefinish',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorhardwarestyle',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorinteriorfinish',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorinteriorspecies',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorlocksensor',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorscreen',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionmarvindoorshade',
            name='optionmarvindoorbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionmarvindoorbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowexteriorcolor',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowhardwarefinish',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowinteriorfinish',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowinteriorspecies',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowlocksensor',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowscreen',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.AlterField(
            model_name='optionwindowshade',
            name='optionwindowbrand',
            field=models.ForeignKey(blank=True, help_text='What is the brand to which this options applies?', null=True, on_delete=django.db.models.deletion.PROTECT, to='esteem.optionwindowbrand'),
        ),
        migrations.CreateModel(
            name='EstisheetHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrysets', models.IntegerField(default=0, help_text='Amount of Entry Sets requested', verbose_name='entry sets')),
                ('entrysetscomments', models.CharField(blank=True, help_text='Comments regarding entry sets', max_length=255, verbose_name='entry sets comments')),
                ('electroniclocks', models.IntegerField(default=0, help_text='Amount of Electronic Locks requested', verbose_name='electronic locks')),
                ('electroniclockscomments', models.CharField(blank=True, help_text='Comments regarding electronic locks', max_length=255, verbose_name='electronic locks comments')),
                ('deadbolts', models.IntegerField(default=0, help_text='Amount of Deadbolts requested', verbose_name='deadbolts')),
                ('deadboltscomments', models.CharField(blank=True, help_text='Comments regarding deadbolts', max_length=255, verbose_name='deadbolts comments')),
                ('keyedknobs', models.IntegerField(default=0, help_text='Amount of Keyed Knobs and Levers requested', verbose_name='keyed knobs')),
                ('keyedknobscomments', models.CharField(blank=True, help_text='Comments regarding keyed knobs', max_length=255, verbose_name='keyed knobs comments')),
                ('knobs', models.IntegerField(default=0, help_text='Amount of non-Keyed Knobs and Levers requested', verbose_name='non-keyed knobs')),
                ('knobscomments', models.CharField(blank=True, help_text='Comments regarding non-keyed knobs', max_length=255, verbose_name='non-keyed knobs comments')),
                ('sideplatelocks', models.IntegerField(default=0, help_text='Amount of Sideplate Locks requested', verbose_name='sideplate locks')),
                ('sideplatelockscomments', models.CharField(blank=True, help_text='Comments regarding side plate locks', max_length=255, verbose_name='side plate locks comments')),
                ('slidingdoorhardware', models.IntegerField(default=0, help_text='Amount of Sliding Door Hardware requested', verbose_name='sliding door hardware')),
                ('slidingdoorhardwarecomments', models.CharField(blank=True, help_text='Comments regarding sliding door hardware', max_length=255, verbose_name='sliding door hardware comments')),
                ('barndoorhardware', models.IntegerField(default=0, help_text='Amount of Barn Door Hardware sets requested', verbose_name='barn door hardware')),
                ('barndoorhardwarecomments', models.CharField(blank=True, help_text='Comments regarding barn door hardware', max_length=255, verbose_name='bard door hardware comments')),
                ('dooraccessories', models.IntegerField(default=0, help_text='Amount of Door Accessories requested', verbose_name='door accessories')),
                ('dooraccessoriescomments', models.CharField(blank=True, help_text='Comments regarding door accessories', max_length=255, verbose_name='door accessories comments')),
                ('estirequest', models.ForeignKey(help_text='For what request is this sheet?', on_delete=django.db.models.deletion.CASCADE, to='esteem.estirequest')),
            ],
            options={
                'verbose_name': 'estimate sheet for hardware',
                'ordering': ('estirequest',),
            },
        ),
    ]
