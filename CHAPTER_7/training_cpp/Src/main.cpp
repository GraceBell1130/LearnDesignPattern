#include "stdafx.h"
#include "duck_interface.hpp"
#include "duck_adapter.hpp"
#include "mallard_duck.hpp"
#include "turkey_interface.hpp"
#include "turkey_adapter.hpp"
#include "wild_turkey.hpp"

#include "amplifier.hpp"
#include "tuner.hpp"
#include "streaming_player.hpp"
#include "cd_player.hpp"
#include "projector.hpp"
#include "theater_lights.hpp"
#include "screen.hpp"
#include "popcorn_popper.hpp"
#include "home_theater_facade.hpp"

void testDuck(std::shared_ptr<Duck> duck) {
	duck->quack();
	duck->fly();
}

int main() {
	std::tcout.imbue(std::locale("korean"));

	std::shared_ptr<Turkey> turkey = std::make_shared<WildTurkey>();
	std::tcout << TEXT("칠면조가 말하길") << std::endl;
	turkey->gobble();
	turkey->fly();

	std::shared_ptr<Duck> duck = std::make_shared<MallardDuck>();
	std::tcout << std::endl << TEXT("오리가 말하길") << std::endl;

	testDuck(duck);
	std::tcout << std::endl << TEXT("칠면조 어댑터가 말하길") << std::endl;
	std::shared_ptr<Duck> turkey_adapter = std::make_shared<TurkeyAdapter>(turkey);
	testDuck(turkey_adapter);

	std::cout << std::endl;

	std::shared_ptr<Amplifier> amplifier = std::make_shared<Amplifier>(TEXT("Amplifier"));
	std::shared_ptr<Tuner> tuner = std::make_shared<Tuner>(TEXT("AM/FM Tuner"));
	std::shared_ptr<StreamingPlayer> streaming_player = std::make_shared<StreamingPlayer>(TEXT("Streaming Player"));
	std::shared_ptr<CdPlayer> cd_player = std::make_shared<CdPlayer>(TEXT("CD Player"), amplifier);
	std::shared_ptr<Projector> projector = std::make_shared<Projector>(TEXT("Projector"));
	std::shared_ptr<TheaterLights> theater_lights = std::make_shared<TheaterLights>(TEXT("Theater Ceiling Lights"));
	std::shared_ptr<Screen> screen = std::make_shared<Screen>(TEXT("Theater Screen"));
	std::shared_ptr<PopcornPopper> popcorn_popper = std::make_shared<PopcornPopper>(TEXT("Popcorn Popper"));
	std::shared_ptr<HomeTheaterFacade> home_theater_facade 
		= std::make_shared<HomeTheaterFacade>(amplifier, tuner, streaming_player, cd_player, projector, screen, theater_lights, popcorn_popper);
	
	home_theater_facade->WatchMovie(TEXT("Raiders of the Lost Ark"));
	std::cout << std::endl;
	home_theater_facade->EndMovie();
}
