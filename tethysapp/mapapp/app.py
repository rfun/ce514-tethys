from tethys_sdk.base import TethysAppBase, url_map_maker


class Mapapp(TethysAppBase):
    """
    Tethys app class for Mapapp.
    """

    name = 'Mapapp'
    index = 'mapapp:home'
    icon = 'mapapp/images/icon.gif'
    package = 'mapapp'
    root_url = 'mapapp'
    color = '#2980b9'
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
                url='mapapp',
                controller='mapapp.controllers.home'
            ),
		UrlMap(
                name='maps',
                url='mapapp/maps',
                controller='mapapp.controllers.maps'
            ),
		UrlMap(
                name='data',
                url='mapapp/data',
                controller='mapapp.controllers.data'
            ),
		UrlMap(
                name='about',
                url='mapapp/about',
                controller='mapapp.controllers.about'
            ),
        )

        return url_maps
