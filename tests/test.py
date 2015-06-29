import sublime, sys
from unittest import TestCase
import sexp
import rpc
from rpc import *

version = sublime.version()

# Contructors are missing
#typeInfo = TypeInfo("type1", 7, DeclaredAs.Method, "FOO.type1", List(), List(), None, Some(8))

#https://github.com/randy3k/UnitTesting

if version<'3000':
    # st2
   ensime =  sys.modules["ensime"]
else:
    # st3
   ensime =  sys.modules["Ensime.ensime"]


class test_internal_functions(TestCase):

	def checkDecode(self, swankStr, parseFn):
		form = sexp.read(swankStr)
		result = parseFn(form)
		self.assertNotEqual(result, None)

	def test_message_deocde(self):
		self.checkDecode(
			"""(:name "name" :local-name "localName" :decl-pos nil :type (:arrow-type nil :name "type1" :type-id 7 :decl-as method :full-name "FOO.type1" :type-args nil :members nil :pos nil :outer-type-id 8) :is-callable nil :owner-type-id 2)""",
			SymbolInfo.parse)

		self.checkDecode("""(:prefix "fooBar" :completions ((:name "name" :type-sig (((("abc" "def") ("hij" "lmn"))) "ABC") :type-id 88 :is-callable nil :relevance 90 :to-insert "BAZ")))""",
			CompletionInfoList.parse)
