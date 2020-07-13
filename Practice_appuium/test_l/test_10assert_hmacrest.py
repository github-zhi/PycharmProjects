from hamcrest import *

def test_hamcrest():
    # assert_that(10, equal_to(10), "这是提示，正确通过，错误才提示。")
    # assert_that(10, equal_to(8), "这是提示，正确通过，错误才提示。")
    assert_that(12, close_to(10, 2)) # 判断前面的值是不是在8-12之间
    assert_that("contains some string", contains_string("string"))
    