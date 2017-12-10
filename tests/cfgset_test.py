#! /usr/bin/env python

import cfgset, contextlib, datetime, logging, logtool, os, unittest
from functools import partial
from path import Path

# logging.basicConfig (level = logging.DEBUG)

class CfgSet_Tests (unittest.TestCase):

  @logtool.log_call
  def test_simplevalue (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section1/one"), 111)

  @logtool.log_call
  def test_inherited (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section1/two"), "two")

  @logtool.log_call
  def test_expanded (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section1/onetwo"), "111two")

  @logtool.log_call
  def test_nestedcompound (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section1/layer"), "111two")

  @logtool.log_call
  def test_override (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section2/l"), "foo")

  @logtool.log_call
  def test_override2 (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section3/sub3a/sub3a1/key"), "sub3a1")

  @logtool.log_call
  def test_override3 (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test1",])
      self.assertEqual (d.value ("section3/sub3b/sub3b1/key"), "onetwo")

###

  @logtool.log_call
  def test_2simplevalue (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section1/one"), 111)

  @logtool.log_call
  def test_2inherited (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section1/two"), "two")

  @logtool.log_call
  def test_2expanded (self):
    with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section1/onetwo"), "111two")

  @logtool.log_call
  def test_2nestedcompound (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section1/layer"), "111two")

  @logtool.log_call
  def test_2override (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section2/l"), "foo")

  @logtool.log_call
  def test_2override2 (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section3/sub3a/sub3a1/key"), "sub3a1")

  @logtool.log_call
  def test_2override3 (self):
     with Path ("tests"):
      d = cfgset.CfgSet (["test2a", "test2b",])
      self.assertEqual (d.value ("section3/sub3b/sub3b1/key"), "onetwo")

if __name__ == "__main__":
  unittest.main()
