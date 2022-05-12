# Generated by Django 4.0.3 on 2022-05-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.TextField()),
                ('ethnicity', models.TextField()),
                ('grade', models.TextField()),
                ('major', models.TextField()),
                ('discussion', models.TextField()),
                ('gpa', models.TextField()),
                ('program', models.TextField()),
                ('professional', models.TextField()),
                ('enrollment', models.TextField()),
                ('prior', models.TextField()),
                ('internship', models.BooleanField()),
                ('research', models.BooleanField()),
                ('parent_engineer', models.BooleanField()),
                ('family_engineer', models.BooleanField()),
                ('previous_school_impact', models.TextField()),
                ('finish_degree', models.TextField()),
                ('finish_degree_here', models.TextField()),
                ('technology_importance', models.TextField()),
                ('parents_disprove_difft', models.TextField()),
                ('engineer_fix_world', models.TextField()),
                ('engineer_paid', models.TextField()),
                ('parents_want', models.TextField()),
                ('job_guarantee', models.TextField()),
                ('faculty_encor', models.TextField()),
                ('mentor_encor', models.TextField()),
                ('intro_opportunity', models.TextField()),
                ('feel_good', models.TextField()),
                ('like_build', models.TextField()),
                ('engineer_fun', models.TextField()),
                ('use_society', models.TextField()),
                ('engineer_interesting', models.TextField()),
                ('figure_out_work', models.TextField()),
                ('mentoring_program', models.TextField()),
                ('Relate', models.TextField()),
                ('lot_common', models.TextField()),
                ('others_share', models.TextField()),
                ('relate_extra', models.TextField()),
                ('succeed', models.TextField()),
                ('well_paying', models.TextField()),
                ('expect', models.TextField()),
                ('lifestyle', models.TextField()),
                ('part_group', models.TextField()),
                ('job', models.TextField()),
                ('like_job', models.TextField()),
                ('bad_test', models.TextField()),
                ('friends', models.TextField()),
                ('cope', models.TextField()),
                ('only_one', models.TextField()),
                ('approach', models.TextField()),
                ('new_env', models.TextField()),
                ('self_confidence', models.TextField()),
                ('leadership', models.TextField()),
                ('public', models.TextField()),
                ('math', models.TextField()),
                ('science', models.TextField()),
                ('communication', models.TextField()),
                ('apply', models.TextField()),
                ('business', models.TextField()),
                ('teams', models.TextField()),
                ('reward', models.TextField()),
                ('study', models.TextField()),
                ('advantage', models.TextField()),
                ('no_care', models.TextField()),
                ('benefit', models.TextField()),
                ('other', models.TextField()),
                ('no_change', models.TextField()),
                ('effort', models.TextField()),
                ('boring', models.TextField()),
            ],
        ),
    ]
