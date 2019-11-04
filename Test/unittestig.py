import unittest
from Helpers.Helpers import filter_by_other_keys, filer_by_tags, filter_by_status
from Handlers.QueryFilter import get_user, get_tickets, get_organization, get_searchable_keys
json = [
    {
        "_id": 1,
        "url": "http://initech.tokoin.io.com/api/v2/users/1.json",
        "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
        "name": "Francisca Rasmussen",
        "alias": "Miss Coffey",
        "created_at": "2016-04-15T05:19:46 -10:00",
        "active": True,
        "verified": True,
        "shared": False,
        "locale": "en-AU",
        "timezone": "Sri Lanka",
        "last_login_at": "2013-08-04T01:03:27 -10:00",
        "email": "coffeyrasmussen@flotonic.com",
        "phone": "8335-422-718",
        "signature": "Don't Worry Be Happy!",
        "organization_id": 119,
        "tags": [
            "Springville",
            "Sutton",
            "Hartsville/Hartley",
            "Diaperville"
        ],
        "suspended": True,
        "role": "admin"
    },
]


class TestHelpers(unittest.TestCase):

    def test_empt_json(self):
        self.assertEqual(filter_by_other_keys(json_object="", keyword="_id", value="1"), [])
        self.assertEqual(filter_by_status(json_object="", keyword="active", value="true"), [])
        self.assertEqual(filer_by_tags(json_object="", keyword="tags", tags="Sutton"), [])

    def test_empty_keyword(self):
        self.assertEqual(filter_by_other_keys(json_object=json, keyword="", value="1"), [])
        self.assertEqual(filter_by_status(json_object=json, keyword="", value="true"), [])
        self.assertEqual(filer_by_tags(json_object=json, keyword="", tags="Sutton"), [])

    def test_value_keyword(self):
        self.assertEqual(filter_by_other_keys(json_object=json, keyword="_id", value=""), [])
        self.assertEqual(filter_by_status(json_object=json, keyword="active", value=""), [])
        self.assertEqual(filer_by_tags(json_object=json, keyword="tags", tags=""), [])

    def test_with_all(self):
        self.assertNotEqual(filter_by_other_keys(json_object=json, keyword="_id", value="1"), list)
        self.assertNotEqual(filter_by_status(json_object=json, keyword="active", value="true"), list)
        self.assertNotEqual(filer_by_tags(json_object=json, keyword="tags", tags="Sutton"), list)


class TestQueryFinder(unittest.TestCase):

    def test_get_user(self):
        self.assertEqual(get_user("", ""), [])
        self.assertEqual(get_user("active", ""), [])
        self.assertEqual(get_user("", "true"), [])
        self.assertNotEqual(get_user("active", "true"), [])
        self.assertNotEqual(get_user("_id", "1"), [])
        self.assertNotEqual(get_user("tags", "Springville"), [])

    def test_get_ticekts(self):
        self.assertEqual(get_tickets("", ""), [])
        self.assertEqual(get_tickets("_id", ""), [])
        self.assertEqual(get_tickets("", "true"), [])
        self.assertNotEqual(get_tickets("_id", "436bf9b0-1147-4c0a-8439-6f79833bff5b"), [])
        self.assertNotEqual(get_tickets("tags", "Ohio"), [])
        self.assertNotEqual(get_tickets("has_incidents", "true"), [])

    def test_get_organizations(self):
        self.assertEqual(get_organization("", ""), [])
        self.assertEqual(get_organization("_id", ""), [])
        self.assertEqual(get_organization("", "101"), [])
        self.assertNotEqual(get_organization("_id", "101"), [])
        self.assertNotEqual(get_organization("tags", "Fulton"), [])
        self.assertNotEqual(get_organization("shared_tickets", "true"), [])

    def test_get_searchable_keys(self):
        self.assertNotEqual(get_searchable_keys(), [])


if __name__ == "__main__":
    unittest.main()
