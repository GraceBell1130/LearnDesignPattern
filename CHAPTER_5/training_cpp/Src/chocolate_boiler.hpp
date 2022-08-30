#pragma once
#include "stdafx.h"

class ChocolateBoiler {
private:
	bool empty;
	bool boiled;
	static std::shared_ptr<ChocolateBoiler> instance;
	static std::mutex mutex;
	 ChocolateBoiler() : empty(true), boiled(false) {
		// method 2
		// instance = std::make_shared<ChocolateBoiler>();
	}

public:
	static std::shared_ptr<ChocolateBoiler> GetInstance() {
		mutex.lock();
		if (0 == instance.use_count()) {
			instance.reset(new ChocolateBoiler());
		}
		mutex.unlock();
		return instance;
	}
	/* method 2
	static std::shared_ptr<ChocolateBoiler> GetInstance() {
		return instance;
	}
	*/

	void Fill() {
		if (IsEmpty()) {
			empty = false;
			boiled = false;
		}
	}

	void Drain() {
		if (false == IsEmpty() && IsBoiled()) {
			empty = true;
		}
	}

	void Boil() {
		if (IsEmpty() && false == IsBoiled()) {
			boiled= true;
		}
	}

	bool IsEmpty() {
		return empty;
	}

	bool IsBoiled() {
		return boiled;
	}
};
std::shared_ptr<ChocolateBoiler> ChocolateBoiler::instance = nullptr;
std::mutex ChocolateBoiler::mutex;
