#pragma once
#include "stdafx.h"

class Stereo {
public:
	Stereo(std::tstring location) {
		location_ = location;
	}

	void On() {
		std::tcout << location_ << TEXT(" ������� �������ϴ�.") << std::endl;
	}

	void Off() {
		std::tcout << location_ << TEXT(" ������� �������ϴ�.") << std::endl;
	}

	void SetCD() {
		std::tcout << location_ << TEXT(" ��������� CD�� ����˴ϴ�.") << std::endl;
	}

	void SetDVD() {
		std::tcout << location_ << TEXT(" ��������� DVD�� ����˴ϴ�.") << std::endl;
	}

	void SetRadio() {
		std::tcout << location_ << TEXT(" ��������� Radio�� ����˴ϴ�.") << std::endl;
	}

	void SetVolume(uint8_t volume) {
		std::tcout << location_ << TEXT(" ������� ������ ") << volume << TEXT("�� �����Ǿ����ϴ�.") << std::endl;
	}


private:
	std::tstring location_;
};