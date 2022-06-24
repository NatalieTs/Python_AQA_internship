from fixture_asserts import soft_assert


def test_check_soft_assert(soft_assert):
    user_data = {'name': 'Sam', 'age': 50, 'gender': 'male'}
    soft_assert.assert_that(user_data['name'], 'Bill')
    soft_assert.assert_that(user_data['age'], 60)
    soft_assert.assert_that(user_data['gender'], 'male')

    soft_assert.assert_all()

def test_check_soft_assert_success(soft_assert):
    user_data = {'name': 'Sam', 'age': 50, 'gender': 'male'}
    soft_assert.assert_that(user_data['name'], 'Sam')
    soft_assert.assert_that(user_data['age'], 50)
    soft_assert.assert_that(user_data['gender'], 'male')

    soft_assert.assert_all()
