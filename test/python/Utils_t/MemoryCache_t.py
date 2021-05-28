#!/usr/bin/env python
"""
Unittests for MemoryCache object
"""

from __future__ import division, print_function

import unittest
from time import sleep

from Utils.MemoryCache import MemoryCache, MemoryCacheException
from Utils.PythonVersion import PY3

class MemoryCacheTest(unittest.TestCase):
    """
    unittest for MemoryCache functions
    """

    def testBasics(self):
        cache = MemoryCache(1, [])
        self.assertCountEqual(cache.getCache(), []) if PY3 else self.assertItemsEqual(cache.getCache(), [])
        cache.setCache(["item1", "item2"])
        self.assertCountEqual(cache.getCache(), ["item1", "item2"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2"])
        # wait for cache to expiry, wait for 2 secs
        sleep(2)
        self.assertRaises(MemoryCacheException, cache.getCache)
        cache.setCache(["item4"])
        # and the cache is alive again
        self.assertCountEqual(cache.getCache(), ["item4"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item4"])

    def testCacheSet(self):
        cache = MemoryCache(2, set())
        self.assertCountEqual(cache.getCache(), set()) if PY3 else self.assertItemsEqual(cache.getCache(), set())
        cache.setCache(set(["item1", "item2"]))
        self.assertCountEqual(cache.getCache(), ["item1", "item2"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2"])
        cache.addItemToCache("item3")
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3"])
        cache.addItemToCache(["item4"])
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3", "item4"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3", "item4"])
        cache.addItemToCache(set(["item5"]))
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3", "item4", "item5"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3", "item4", "item5"])
        self.assertTrue("item2" in cache)
        self.assertFalse("item222" in cache)

    def testCacheList(self):
        cache = MemoryCache(2, [])
        self.assertCountEqual(cache.getCache(), []) if PY3 else self.assertItemsEqual(cache.getCache(), [])
        cache.setCache(["item1", "item2"])
        self.assertCountEqual(cache.getCache(), ["item1", "item2"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2"])
        cache.addItemToCache("item3")
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3"])
        cache.addItemToCache(["item4"])
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3", "item4"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3", "item4"])
        cache.addItemToCache(set(["item5"]))
        self.assertCountEqual(cache.getCache(), ["item1", "item2", "item3", "item4", "item5"]) if PY3 else self.assertItemsEqual(cache.getCache(), ["item1", "item2", "item3", "item4", "item5"])
        self.assertTrue("item2" in cache)
        self.assertFalse("item222" in cache)

    def testCacheDict(self):
        cache = MemoryCache(2, {})
        self.assertCountEqual(cache.getCache(), {}) if PY3 else self.assertItemsEqual(cache.getCache(), {})
        cache.setCache({"item1": 11, "item2": 22})
        self.assertCountEqual(cache.getCache(), {"item1": 11, "item2": 22}) if PY3 else self.assertItemsEqual(cache.getCache(), {"item1": 11, "item2": 22})
        cache.addItemToCache({"item3": 33})
        self.assertCountEqual(cache.getCache(), {"item1": 11, "item2": 22, "item3": 33}) if PY3 else self.assertItemsEqual(cache.getCache(), {"item1": 11, "item2": 22, "item3": 33})
        self.assertTrue("item2" in cache)
        self.assertFalse("item222" in cache)
        # test exceptions
        self.assertRaises(TypeError, cache.addItemToCache, "item4")
        self.assertRaises(TypeError, cache.addItemToCache, ["item4"])

    def testSetDiffTypes(self):
        cache = MemoryCache(2, set())
        self.assertCountEqual(cache.getCache(), set()) if PY3 else self.assertItemsEqual(cache.getCache(), set())
        cache.setCache({"item1", "item2"})
        self.assertRaises(TypeError, cache.setCache, ["item3"])


if __name__ == "__main__":
    unittest.main()