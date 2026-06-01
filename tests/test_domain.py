import numpy as np
import pytest
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

from cromosim.domain import Destination, Domain


def test_create_domain():
    width, height = 600, 400
    dom = Domain(name='room', pixel_size=0.1, width=width, height=height,
                 wall_colors=[[0, 0, 0]])

    circle = Circle((30.0, 20.0), 2.0)
    dom.add_shape(circle, outline_color=[0, 0, 0], fill_color=[0, 0, 0])

    line = Line2D([17.0, 23.0], [3.1, 3.1], linewidth=2)
    dom.add_shape(line, outline_color=[255, 0, 0], fill_color=[255, 0, 0])

    dom.build_domain()
    assert dom.image.shape == (height, width, 3)

    dest = Destination(name='door', colors=[[255, 0, 0]],
                       excluded_colors=[[0, 0, 0]])
    dom.add_destination(dest)
    assert 'door' in dom.destinations
    assert dom.destinations['door'].distance is not None


def test_domain_no_walls_raises():
    dom = Domain(name='empty', pixel_size=1.0, width=50, height=50,
                 wall_colors=[[0, 0, 0]])
    with pytest.raises(RuntimeError, match="No wall pixels"):
        dom.build_domain()


def test_domain_str():
    dom = Domain(name='test', pixel_size=0.5, width=100, height=80)
    assert 'test' in str(dom)


def test_destination_str():
    dest = Destination(name='exit', colors=[[255, 0, 0]])
    assert 'exit' in str(dest)
