#pragma once
#include "stdafx.h"

class StreamingPlayer {
public:
	StreamingPlayer(std::tstring description) {
		description_ = description;
	}

	void On() {
		std::tcout << description_ << TEXT(" on") << std::endl;
	}

	void Off() {
		std::tcout << description_ << TEXT(" off") << std::endl;
	}

	void Play(std::tstring movie) {
		movie_ = movie;
		current_chapter_ = 0;
		std::tcout << description_ << TEXT(" playing \"") << movie << TEXT("\"") << std::endl;
	}

	void Play(int chapter) {
		if (movie_.empty()) {
			std::tcout << description_ << TEXT(" can't play chapter ") << chapter << TEXT(" no movie selected") << std::endl;
		} else {
			current_chapter_ = chapter;
			std::tcout << description_ << TEXT(" playing chapter ") << current_chapter_ << TEXT("of \"") << movie_ << TEXT("\"") << std::endl;
		}
	}

	void Stop() {
		current_chapter_ = 0;
		std::tcout << description_ << TEXT(" stopped \"") << movie_ << TEXT("\"") << std::endl;
	}

	void Pause() {
		std::tcout << description_ << TEXT(" paused \"") << movie_ << TEXT("\"") << std::endl;
	}

	void SetTwoChannelAudio() {
		std::tcout << description_ << TEXT(" set two channel audio") << std::endl;
	}

	void SetSurroundAudio() {
		std::tcout << description_ << TEXT(" set surround audio") << std::endl;
	}

	std::tstring ToString() {
		return description_;
	}

private:
	std::tstring description_;
	std::tstring movie_;
	int current_chapter_;
};