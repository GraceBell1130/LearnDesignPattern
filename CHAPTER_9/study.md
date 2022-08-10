객체 컬렌션에서 remove 메소드를 반드시 제공해야할 필요는 없음

**반복자 패턴(Iterator Pattern) : 컬렉션의 구현 방법을 노출하지 않으면서 집합체 내의 모든 항목에 접근하는 방법**
- 집합체 내에서 어떤 식으로 일이 처리되는지 전혀 모르는 상태에서 그 안에 들어있는 모든 항목을 대상으로 반복 작업을 수행할 수 있음
- 컬렉션 객체 안에 들어있는 모든 항목에 접근하는 방식이 통일되어 있으면 종류에 관계없이 모든 집합체에 사용할 수 있는 다형적인 코드를 만들 수 있음


디자인 원칙
8. 단일 역할 원칙 : 어떤 클래스가 바뀌는 이유는 하나뿐이어야 한다.
- 하나의 클래스는 하나의 역할만 맡아야 함

응집도 : 한 클래스 또는 모듈이 특정 목적이나 역할을 얼마나 일관되게 지원하는지를 나타내는 척도


**컴포지트 패턴(Composite Pattern) : 클라이언트에서 개별 객체와 복합 객체를 똑같은 방법으로 다룰 수 있음**
- 객체를 트리구조로 구성해서 부분-전체 계층구조를 구현합니다. 
- 단일 역할 원칙을 깨는 대신 투명성을 확보한 패턴
- 클라이언트를 단순화시킬 수 있는 장점이 있음

부분-전체 계층구조(part-whole hierarchy) : 부분들이 계층을 이루고 있지만 모든 부분을 묶어서 전체로 다룰 수 있는 구조  

투명성 (transparency) : 어떤 원소가 복합 객체인지 잎인지가 클라이언트에게 투명하게 보이는 것
