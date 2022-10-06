#pragma once
#include "stdafx.h"
#include "tuner.hpp"
#include "amplifier.hpp"

class CdPlayer {
public:
	CdPlayer(std::tstring description, std::shared_ptr<Amplifier> amplifier) {
		description_ = description;
		amplifier_ = amplifier;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void Eject() {
		title_ = TEXT("");
		std::tcout << description_ << TEXT(" eject") << std::endl;
	}

	void Play(std::tstring title) {
		title_ = title;
		current_track_ = 0;
		std::tcout << description_ << TEXT(" playing \"") << title_ << TEXT("\"") << std::endl;
	}

	void Play(int track) {
		if (title_.empty()) {
			std::tcout << description_ << TEXT(" can't play track ") << current_track_ << TEXT(", no cd inserted") << std::endl;
		} else {
			current_track_ = track;
			std::tcout << description_ << TEXT(" playing track ") << current_track_ << std::endl;
		}
	}

	void Stop() {
		current_track_ = 0;
		std::tcout << description_ << TEXT(" stopped") << std::endl;
	}

	void Pause() {
		std::tcout << description_ << TEXT(" paused \"") << title_ << TEXT("\"") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
	std::tstring title_;
	int current_track_;
	std::shared_ptr<Amplifier> amplifier_;

};