#pragma once
#include "stdafx.h"

class Stereo {
public:
	Stereo(std::tstring location) {
		location_ = location;
	}

	void On() {
		std::tcout << location_ << TEXT(" 오디오가 켜졌습니다.") << std::endl;
	}

	void Off() {
		std::tcout << location_ << TEXT(" 오디오가 꺼졌습니다.") << std::endl;
	}

	void SetCD() {
		std::tcout << location_ << TEXT(" 오디오에서 CD가 재생됩니다.") << std::endl;
	}

	void SetDVD() {
		std::tcout << location_ << TEXT(" 오디오에서 DVD가 재생됩니다.") << std::endl;
	}

	void SetRadio() {
		std::tcout << location_ << TEXT(" 오디오에서 Radio가 재생됩니다.") << std::endl;
	}

	void SetVolume(uint8_t volume) {
		std::tcout << location_ << TEXT(" 오디오의 볼륨이 ") << volume << TEXT("로 설정되었습니다.") << std::endl;
	}


private:
	std::tstring location_;
};