#pragma once
#include "stdafx.h"
#include "amplifier.hpp"
#include "tuner.hpp"
#include "streaming_player.hpp"
#include "cd_player.hpp"
#include "projector.hpp"
#include "theater_lights.hpp"
#include "screen.hpp"
#include "popcorn_popper.hpp"

class HomeTheaterFacade {
public:
	HomeTheaterFacade(
		std::shared_ptr<Amplifier> amplifier,
		std::shared_ptr<Tuner> tuner,
		std::shared_ptr<StreamingPlayer> streaming_player,
		std::shared_ptr<CdPlayer> cd_player,
		std::shared_ptr<Projector> projector,
		std::shared_ptr<Screen> screen,
		std::shared_ptr<TheaterLights> theater_lights,
		std::shared_ptr<PopcornPopper> popcorn_popper) {
		amplifier_ = amplifier;
		tuner_ = tuner;
		streaming_player_ = streaming_player;
		cd_player_ = cd_player;
		projector_ = projector;
		screen_ = screen;
		theater_lights_ = theater_lights;
		popcorn_popper_ = popcorn_popper;
	}

	void WatchMovie(std::tstring movie) {
		std::tcout << TEXT("Get ready to watch a movie...") << std::endl;
		popcorn_popper_->On();
		popcorn_popper_->Pop();

		theater_lights_->Dim(10);
		screen_->Down();
		projector_->On();
		projector_->WideScreenMode();
		amplifier_->On();
		amplifier_->SetStreamingPlayer(streaming_player_);
		amplifier_->SetSurroundSound();
		amplifier_->SetVolume(5);
		streaming_player_->On();
		streaming_player_->Play(movie);
	}

	void EndMovie() {
		std::tcout << TEXT("Shutting movie theater down...") << std::endl;

		popcorn_popper_->Off();
		theater_lights_->On();
		screen_->Up();
		projector_->Off();
		amplifier_->Off();
		streaming_player_->Stop();
		streaming_player_->Off();
	}

	void ListenToRadio(double frequency) {
		std::tcout << TEXT("Tuning in the airwaves...") << std::endl;
		tuner_->On();
		tuner_->SetFrequency(frequency);
		amplifier_->On();
		amplifier_->SetVolume(5);
		amplifier_->SetTuner(tuner_);
	}

	void EndRadio() {
		std::tcout << TEXT("Shutting down the tuner...") << std::endl;
		tuner_->Off();
		amplifier_->Off();
	}

private:
	std::shared_ptr<Amplifier> amplifier_;
	std::shared_ptr<Tuner> tuner_;
	std::shared_ptr<StreamingPlayer> streaming_player_;
	std::shared_ptr<CdPlayer> cd_player_;
	std::shared_ptr<Projector> projector_;
	std::shared_ptr<TheaterLights> theater_lights_;
	std::shared_ptr<Screen> screen_;
	std::shared_ptr<PopcornPopper> popcorn_popper_;
};