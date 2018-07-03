import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/px-uploader'

class TestAsciichPXUploaderImage(object):

    def test_pxuploader_installed(self, docker_container):
        assert docker_container.image.name == 'asciich/px-uploader'
        assert docker_container.exists('px_uploader')
