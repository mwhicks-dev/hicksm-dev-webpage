/*<![CDATA[*/

var app = angular.module( "portfolioSite", [] );
app.controller( "headerCtrl", function( $scope, $rootScope, $http, $q ) {

    $rootScope.setup = function( title ) {

        var root_dir = ( title == 'Home' )
            ? '.'
            : '..';

        $rootScope.nav_menu_components = {
            'Home' : root_dir + '/index.html',
            'Programming Projects' : root_dir + '/programming-projects/programming-projects.html',
            'Resume' : root_dir + '/resume/resume.html',
            'Nick' : root_dir + '/nick/nick.html'
        }

        $rootScope.nav_menu_components[ title ] = '#';

        $rootScope.title = title;

    };

    $rootScope.$on( 'setTitle', function( event, data ) {

        console.log( 'Hit!' );

        $rootScope.setup( data.title );

    });

});

/*]]>*/
