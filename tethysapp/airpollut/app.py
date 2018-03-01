from tethys_sdk.base import TethysAppBase, url_map_maker


class Airpollut(TethysAppBase):
    """
    Tethys app class for Air Quality Prediction.
    """

    name = 'Air Quality Prediction'
    index = 'airpollut:home'
    icon = 'airpollut/images/icon.gif'
    package = 'airpollut'
    root_url = 'airpollut'
    color = '#64b5f6'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='airpollut',
                controller='airpollut.controllers.home'
            ),
        )

        return url_maps
