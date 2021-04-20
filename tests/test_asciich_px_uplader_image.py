import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/px-uploader'

class TestAsciichPXUploaderImage(object):

    def test_python_interpreter_exists(self, docker_container):
        assert docker_container.exists('python')

    def test_pxuploader_installed(self, docker_container):
        assert docker_container.image.name == 'asciich/px-uploader'
        assert docker_container.exists('px_uploader')

    def test_px_uploader_with_no_arguments(self, docker_container):
        with pytest.raises(Exception) as e:
            docker_container.check_output('px_uploader')

        exception_message = str(e)
        assert 'DockerContainerExecError(' in exception_message
        assert 'px_uploader: error: the following arguments are required: --port, firmware' in exception_message
