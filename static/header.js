/*<![CDATA[*/

var app = angular.module( "portfolioSite", [] );
app.controller( "headerCtrl", function( $scope, $rootScope, $http, $q ) {

    $rootScope.setup = function( title ) {

        $rootScope.nav_menu_components = {
            'Home' : 'index.html',
            'Programming Projects' : 'programming-projects.html',
            'Resume' : 'resume.html',
            'Nick' : 'nick.html'
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
