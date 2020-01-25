from django.test import TestCase
from excavation.models import *
import datetime


class AboutModelTestCase(TestCase):
    def setUp(self):
        About.objects.create(editor="Ken", description="Welcome to Kaunos")
        Contact.objects.create(editor="Agnes", description="Tel No: 999 999 9999")
        Topography.objects.create(editor="Cristina", description="Acropolis")
        History.objects.create(editor="Ken", description="Kaunos")
        Monument.objects.create(name="Kaunos",
                                editor="Agnes",
                                images="mon.jpg",
                                short_description="First_monument",
                                description="Kaunos monument of 3BC",
                                slug="kaunos")
        Area.objects.create(name="San Fran",
                            images="san_fran.jpg",
                            short_description="Area of San Fran",
                            description="San Fran area discovered in 1970",
                            slug="san_fran")


    def createAboutInfo(self, editor=" Editor's name", description="Welcome to Kaunos"):
        return About.objects.create(editor=editor, description=description)

    def test_about_info(self):
        obj1 = About.objects.get(editor="Ken")
        self.assertEqual(obj1.editor, "Ken")
        self.assertEqual(obj1.description, "Welcome to Kaunos")

    def test_contact_info(self):
        obj1 = Contact.objects.get(editor="Agnes")
        self.assertEqual(obj1.editor, "Agnes")
        self.assertEqual(obj1.description, "Tel No: 999 999 9999")

    def test_topography_info(self):
        obj1 = Topography.objects.get(editor="Cristina")
        self.assertEqual(obj1.editor, "Cristina")
        self.assertEqual(obj1.description, "Acropolis")

    def test_history_info(self):
        obj1 = History.objects.get(editor="Ken")
        self.assertEqual(obj1.editor, "Ken")
        self.assertEqual(obj1.description, "Kaunos")

    def test_monument_info(self):
        obj1 = Monument.objects.get(name="Kaunos")
        self.assertEqual(obj1.name, "Kaunos")
        self.assertEqual(obj1.editor, "Agnes")
        self.assertEqual(obj1.images, "mon.jpg")
        self.assertEqual(obj1.short_description, "First_monument")
        self.assertEqual(obj1.description, "Kaunos monument of 3BC")
        self.assertEqual(obj1.slug, "kaunos")

    def test_area_info(self):
        obj1 = Area.objects.get(name="San Fran")
        self.assertEqual(obj1.name, "San Fran")
        self.assertEqual(obj1.images, "san_fran.jpg")
        self.assertEqual(obj1.short_description, "Area of San Fran")
        self.assertEqual(obj1.description, "San Fran area discovered in 1970")
        self.assertEqual(obj1.slug, "san_fran")

    def test_trench_info(self):
        Trench.objects.create(name="San Hose",
                              editor="Cristina",
                              area=Area.objects.create(name="San Fran"),
                              images="san_hose.jpg",
                              short_description="Trench of San Hose",
                              description="San Hose trench discovered in 5BC",
                              slug="san_hose",
                              latitude=0,
                              longitude=0
                              )

        obj1 = Trench.objects.get(name="San Hose")
        self.assertEqual(obj1.name, "San Hose")
        self.assertEqual(obj1.editor, "Cristina")
        self.assertEqual(obj1.area.name, "San Fran")
        self.assertEqual(obj1.images, "san_hose.jpg")
        self.assertEqual(obj1.short_description, "Trench of San Hose")
        self.assertEqual(obj1.description, "San Hose trench discovered in 5BC")
        self.assertEqual(obj1.slug, "san_hose")
        self.assertEqual(obj1.latitude, 0)
        self.assertEqual(obj1.longitude, 0)

    def test_building_info(self):
        Building.objects.create(name="San Hose Building",
                                editor="Cristina",
                                area=Area.objects.create(name="San Fran"),
                                object="Copper",
                                images="san_hose_build.jpg",
                                short_description="Building of San Hose",
                                description="San Hose building discovered in 5BC",
                                slug="san_hose_building",
                                latitude=0,
                                longitude=0,
                                width=0.0,
                                height=0.0,
                                depth=0.0,
                                entry_date="2020-01-18 13:55:00+0500",
                                archaeological_date="5 BC"
                              )

        obj1 = Building.objects.get(name="San Hose Building")
        self.assertEqual(obj1.name, "San Hose Building")
        self.assertEqual(obj1.editor, "Cristina")
        self.assertEqual(obj1.area.name, "San Fran")
        self.assertEqual(obj1.object, "Copper")
        self.assertEqual(obj1.images, "san_hose_build.jpg")
        self.assertEqual(obj1.short_description, "Building of San Hose")
        self.assertEqual(obj1.description, "San Hose building discovered in 5BC")
        self.assertEqual(obj1.slug, "san_hose_building")
        self.assertEqual(obj1.latitude, 0)
        self.assertEqual(obj1.longitude, 0)
        self.assertEqual(obj1.width, 0.0)
        self.assertEqual(obj1.height, 0.0)
        self.assertEqual(obj1.depth, 0.0)
        time = obj1.entry_date
        self.assertEqual(obj1.entry_date, time)
        self.assertEqual(obj1.archaeological_date, "5 BC")

    def test_finding_info(self):
        """
        #trench=Trench.objects.create(name=""),
        #building=Building.objects.create(name=""),
        These two fields are optional we are testing Null= True
        #self.assertEqual(obj1.trench.name, "")
        #self.assertEqual(obj1.building.name, "")
        """

        Finding.objects.create(name="San Hose Finding",
                               editor="Ken",
                               area=Area.objects.create(name="San Fran"),
                               object="Copper",
                               images="san_hose_finding.jpg",
                               short_description="Finding of San Hose",
                               description="San Hose finding discovered in 5BC",
                               slug="san_hose_finding",
                               latitude=0,
                               longitude=0,
                               width=0.0,
                               height=0.0,
                               depth=0.0,
                               entry_date="2020-01-18 13:55:00+0500",
                               archaeological_date="5 BC"
                              )

        obj1 = Finding.objects.get(name="San Hose Finding")
        self.assertEqual(obj1.name, "San Hose Finding")
        self.assertEqual(obj1.editor, "Ken")
        self.assertEqual(obj1.area.name, "San Fran")
        self.assertEqual(obj1.object, "Copper")
        self.assertEqual(obj1.images, "san_hose_finding.jpg")
        self.assertEqual(obj1.short_description, "Finding of San Hose")
        self.assertEqual(obj1.description, "San Hose finding discovered in 5BC")
        self.assertEqual(obj1.slug, "san_hose_finding")
        self.assertEqual(obj1.latitude, 0)
        self.assertEqual(obj1.longitude, 0)
        self.assertEqual(obj1.width, 0.0)
        self.assertEqual(obj1.height, 0.0)
        self.assertEqual(obj1.depth, 0.0)
        time = obj1.entry_date
        self.assertEqual(obj1.entry_date, time)
        self.assertEqual(obj1.archaeological_date, "5 BC")

    def test_find_info(self):
        """
        These three fields are optional we are testing Null= True

        #finding=Find.objects.create(name="")
        #trench=Trench.objects.create(name=""),
        #building=Building.objects.create(name=""),

        #self.assertEqual(obj1.finding.name, "")
        #self.assertEqual(obj1.trench.name, "")
        #self.assertEqual(obj1.building.name, "")
        """

        Find.objects.create(name="San Hose Find",
                            editor="Ken",
                            area=Area.objects.create(name="San Fran"),
                            depository="Black",
                            material="Silver",
                            object="Copper",
                            images="san_hose_find.jpg",
                            short_description="Find of San Hose",
                            description="San Hose find discovered in 5BC",
                            slug="san_hose_find",
                            latitude=0,
                            longitude=0,
                            width=0.0,
                            height=0.0,
                            depth=0.0,
                            diameter=0.0,
                            entry_date="2020-01-18 13:55:00+0500",
                            archaeological_date="5 BC"
                            )

        obj1 = Find.objects.get(name="San Hose Find")
        self.assertEqual(obj1.name, "San Hose Find")
        self.assertEqual(obj1.editor, "Ken")
        self.assertEqual(obj1.area.name, "San Fran")
        self.assertEqual(obj1.depository, "Black")
        self.assertEqual(obj1.material, "Silver")
        self.assertEqual(obj1.object, "Copper")
        self.assertEqual(obj1.images, "san_hose_find.jpg")
        self.assertEqual(obj1.short_description, "Find of San Hose")
        self.assertEqual(obj1.description, "San Hose find discovered in 5BC")
        self.assertEqual(obj1.slug, "san_hose_find")
        self.assertEqual(obj1.latitude, 0)
        self.assertEqual(obj1.longitude, 0)
        self.assertEqual(obj1.width, 0.0)
        self.assertEqual(obj1.height, 0.0)
        self.assertEqual(obj1.depth, 0.0)
        self.assertEqual(obj1.diameter, 0.0)
        time = obj1.entry_date
        self.assertEqual(obj1.entry_date, time)
        self.assertEqual(obj1.archaeological_date, "5 BC")