def test_check(expected, result, testname):
    if result  == expected:
        print('✅ SUCCESS - ' + testname)
    else:
        print('❌ FAILURE - ' + testname)
        print('Output: ' + str(result))