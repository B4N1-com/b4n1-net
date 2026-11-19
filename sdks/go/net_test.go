package b4n1net

import (
	"strings"
	"testing"
)

// These tests are offline: they exercise the bundled engine, never the network.

func newClient(t *testing.T) *Client {
	t.Helper()
	client, err := New()
	if err != nil {
		t.Fatalf("engine should resolve on a bundled platform: %v", err)
	}
	return client
}

func TestVersionMatchesEngine(t *testing.T) {
	out, err := newClient(t).Version()
	if err != nil {
		t.Fatalf("version: %v", err)
	}
	if !strings.Contains(out, "v0.4.1") {
		t.Fatalf("unexpected version banner: %q", out)
	}
	if Version != "0.4.1" {
		t.Fatalf("SDK version drifted from the engine: %q", Version)
	}
}

func TestStatusIsReadableWhenStopped(t *testing.T) {
	out, _ := newClient(t).Status(true)
	if out == "" {
		t.Fatal("status produced no output; not running is still a valid state")
	}
}

func TestDemoDoesARealRoundTrip(t *testing.T) {
	out, err := newClient(t).Demo(false)
	if err != nil {
		t.Fatalf("demo: %v", err)
	}
	if !strings.Contains(out, "acknowledged") {
		t.Fatalf("demo did not acknowledge frames: %q", out)
	}
}

func TestManualIsBundled(t *testing.T) {
	out, err := newClient(t).Docs("")
	if err != nil {
		t.Fatalf("docs: %v", err)
	}
	if !strings.Contains(strings.ToLower(out), "quickstart") {
		t.Fatalf("manual missing its quickstart section: %q", out)
	}
}

func TestLicensesNeedNoKey(t *testing.T) {
	out, err := newClient(t).Licenses()
	if err != nil || out == "" {
		t.Fatalf("licenses must print without a key: %v", err)
	}
}
