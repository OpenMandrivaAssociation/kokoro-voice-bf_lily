Name:		kokoro-voice-bf_lily
Version:	1.0
Release:	1
Summary:	British English female Kokoro voice bf_lily
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-en
Provides:	kokoro-voice-en_GB
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/bf_lily.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses the misaki English lexicon.
Select it with: kokoro -m bf_lily

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/bf_lily.pt

%files
%{_datadir}/kokoro/voices/bf_lily.pt
