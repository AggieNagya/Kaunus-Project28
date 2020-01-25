from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from caunus.utils import unique_slug_generator


class HomePage(models.Model):
    header = models.CharField(max_length=250)
    editor = models.CharField(max_length=250)
    description = models.TextField()

    # TODO: Add support for files
    def __str__(self):
        return self.header


class About(models.Model):
    editor = models.CharField(max_length=250)
    description = models.TextField()

    # TODO: Add support for files
    def __str__(self):
        return self.description


class Contact(models.Model):
    editor = models.CharField(max_length=250)
    description = models.TextField()

    # TODO: Add support for files
    def __str__(self):
        return self.description


class Topography(models.Model):
    editor = models.CharField(max_length=250)
    description = models.TextField()

    # TODO: Add support for files
    def __str__(self):
        return self.description


class History(models.Model):
    editor = models.CharField(max_length=250)
    description = models.TextField()

    # TODO: Add support for files
    def __str__(self):
        return self.description

class Monument(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    editor = models.CharField(max_length=250, help_text='editör')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True)  #Added slug for detail view

    # TODO: Add support for files

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('monument_detail', kwargs={'slug': self.slug})  # new


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(slug_save, sender=Monument)


class Area(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True) # Added slug for detail view

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('area_detail', kwargs={'slug': self.slug})  # new


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)
pre_save.connect(slug_save, sender=Area)


class Trench(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    editor = models.CharField(max_length=250, help_text='editör')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, help_text='alan')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True)  #Added slug for detail view
    latitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='enlem')
    longitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='boylam')

    # TODO: Add support for files

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trench_detail', kwargs={'slug': self.slug})  # new


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(slug_save, sender=Trench)


class Building(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    editor = models.CharField(max_length=250, help_text='editör')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, help_text='alan')
    object = models.CharField(max_length=250, help_text='nesne')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True)  # Added slug for detail view
    latitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='enlem')
    longitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='boylam')
    width = models.FloatField(default=0, help_text='genişlik/m')
    height = models.FloatField(default=0, help_text='sekiz/m')
    depth = models.FloatField(default=0, help_text='derinlik/m')
    entry_date = models.DateTimeField(help_text='giriş tarihi')
    archaeological_date = models.CharField(max_length=250, help_text='arkeolojik tarih')

    # TODO: Add support for files

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('building_detail', kwargs={'slug': self.slug})  # new

    class Meta:
        unique_together =('name', 'slug')


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)
pre_save.connect(slug_save, sender=Building)


class Finding(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    editor = models.CharField(max_length=250, help_text='editör')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, help_text='alan')
    trench = models.ForeignKey(Trench, on_delete=models.CASCADE, blank=True, null=True, help_text='hendek')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True, help_text='bina')
    object = models.CharField(max_length=250, help_text='nesne')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True)  # Added slug for detail view
    latitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='enlem')
    longitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='boylam')
    width = models.FloatField(default=0, help_text='genişlik/m')
    height = models.FloatField(default=0, help_text='sekiz/m')
    depth = models.FloatField(default=0, help_text='derinlik/m')
    entry_date = models.DateTimeField(help_text='giriş tarihi')
    archaeological_date = models.CharField(max_length=250, help_text='arkeolojik tarih')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('finding_detail', kwargs={'slug': self.slug})  # new


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)
pre_save.connect(slug_save, sender=Finding)


class Find(models.Model):
    name = models.CharField(max_length=250, help_text='Ad')
    editor = models.CharField(max_length=250, help_text='editör')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, help_text='alan')
    finding = models.ForeignKey(Finding, on_delete=models.CASCADE, blank=True, null=True, help_text='bulgu')
    trench = models.ForeignKey(Trench, on_delete=models.CASCADE, blank=True, null=True, help_text='hendek')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True, help_text='bina')
    depository = models.CharField(max_length=250, help_text='emanetçi')
    material = models.CharField(max_length=250, help_text='malzeme')
    object = models.CharField(max_length=250, help_text='nesne')
    images = models.ImageField(upload_to='pics', help_text='Görüntüler')
    short_description = models.CharField(max_length=250, help_text='Kısa Açıklama')
    description = models.TextField(help_text='aÇiklama')
    slug = models.SlugField(null=False, unique=True)  # Added slug for detail view
    latitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='enlem')
    longitude = models.DecimalField(max_digits=18, decimal_places=15, default=0, help_text='boylam')
    width = models.FloatField(default=0, help_text='genişlik/m')
    height = models.FloatField(default=0, help_text='sekiz/m')
    depth = models.FloatField(default=0, help_text='derinlik/m')
    diameter = models.FloatField(default=0, help_text='çap/m')
    entry_date = models.DateTimeField(help_text='giriş tarihi')
    archaeological_date = models.CharField(max_length=250, help_text='arkeolojik tarih')

    # TODO: Add support for files
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('find_detail', kwargs={'slug': self.slug})


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)
pre_save.connect(slug_save, sender=Find)