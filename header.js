/*<![CDATA[*/

var app = angular.module( "portfolioSite", [] );
app.controller( "headerCtrl", function( $scope, $rootScope, $http, $q ) {

    $rootScope.setup = function( title ) {

        if ( title == 'Home' ) {

            $rootScope.nav_menu_components = {
                'Home' : './index.html',
                'Programming Projects' : './programming-projects/programming-projects.html',
                'Resume' : './resume/resume.html',
                'Nick' : './nick/nick.html'
            }

        } else {  // TODO: Set . -> .. if NOT home

            $rootScope.nav_menu_components = {
                'Home' : '../index.html',
                'Programming Projects' : '../programming-projects/programming-projects.html',
                'Resume' : '../resume/resume.html',
                'Nick' : '../nick/nick.html'
            }

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
