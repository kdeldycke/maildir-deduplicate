# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2015 Kevin Deldycke <kevin@deldycke.com>
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import unittest

from click.testing import CliRunner

from maildir_deduplicate.cli import cli


class CLITestCase(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()


class TestCLI(CLITestCase):

    def test_main_help(self):
        result = self.runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('--help', result.output)


class TestDeduplicateCLI(CLITestCase):

    def test_deduplicate_help(self):
        result = self.runner.invoke(cli, ['deduplicate', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('--help', result.output)


class TestHashCLI(CLITestCase):

    def test_hash_help(self):
        result = self.runner.invoke(cli, ['hash', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('--help', result.output)
