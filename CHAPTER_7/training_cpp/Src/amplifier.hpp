#pragma once
#include "stdafx.h"
#include "tuner.hpp"
#include "streaming_player.hpp"

class Amplifier {
public:
	Amplifier(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void SetStereoSound() {
		std::tcout << description_ << TEXT(" stereo mode on") << std::endl;
	}

	void SetSurroundSound() {
		std::tcout << description_ << TEXT(" surround sound on (5 speakers, 1 subwoofer)") << std::endl;
	}

	void SetVolume(int level) {
		std::tcout << description_ << TEXT(" setting volume to ") << level << std::endl;
	}

	void SetTuner(std::shared_ptr<Tuner> tuner) {
		std::tcout << description_ << TEXT(" setting tuner to ") << tuner->ToString() << std::endl;
		tuner_ = tuner;
	}

	void SetStreamingPlayer(std::shared_ptr<StreamingPlayer> player) {
		std::tcout << description_ << TEXT(" setting Streaming player to ") << player->ToString() << std::endl;
		player_ = player;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
	std::shared_ptr<Tuner> tuner_;
	std::shared_ptr<StreamingPlayer> player_;
};