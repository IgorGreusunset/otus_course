from unittest import TestCase
import secondhomework
from unittest.mock import patch, Mock


class TestMove(TestCase):
    @patch('secondhomework.Movable', autospec=True)
    def test_move(self, mock_movable):
        movable = mock_movable()

        # Test normal case
        movable.get_position = Mock(return_value=(12, 5))
        movable.get_velocity = Mock(return_value=(-7, 3))
        movable.set_position = Mock()

        secondhomework.Move.execute(movable)

        movable.set_position.assert_called_with(5, 8)

        # Test without position
        movable.get_position = Mock(return_value=None)
        self.assertRaises(ValueError, secondhomework.Move.execute, movable)

        # Test without velocity
        movable.get_position = Mock(return_value=(12, 5))
        movable.get_velocity = Mock(return_value=None)
        self.assertRaises(ValueError, secondhomework.Move.execute, movable)


class TestRotate(TestCase):
    @patch('secondhomework.Rotable', autospec=True)
    def test_rotate(self, mock_rotable):
        rotable = mock_rotable()

        # Test normal case
        rotable.get_direction = Mock(return_value=5)
        rotable.get_angular_velocity = Mock(return_value=4)
        rotable.get_directions_number = Mock(return_value=8)
        rotable.set_direction = Mock()

        secondhomework.Rotate.execute(rotable)

        rotable.set_direction.assert_called_with(1)







