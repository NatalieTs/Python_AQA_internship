from fixture_asserts import hard_assert


def test_check_hard_assert(hard_assert):
    user_data = {'name': 'Sam', 'age': 50, 'gender': 'male'}
    hard_assert.assert_that(user_data['name'], 'Bill')
    hard_assert.assert_that(user_data['age'], 60)
    hard_assert.assert_that(user_data['gender'], 'male')


