// Package b4n1net is the Go SDK for the sovereign transport engine.
//
// The module ships the engine for each supported platform under bin/ and
// resolves the one that matches this machine. Every call is a thin spawn into
// that binary: the SDK never reimplements the wire protocol, so an engine fix
// reaches every language at once.
//
//	client, err := b4n1net.New()
//	if err != nil { log.Fatal(err) }
//	fmt.Println(client.Version())
//
// Override the engine with B4N1NET_BIN_PATH.
package b4n1net

import (
	"errors"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
)

// Version is the SDK version; it tracks the engine release.
const Version = "0.4.2"

var binaries = map[string]string{
	"linux/amd64":   "b4n1net-linux-amd64",
	"linux/arm64":   "b4n1net-linux-arm64",
	"darwin/amd64":  "b4n1net-macos-x64",
	"darwin/arm64":  "b4n1net-macos-arm64",
	"windows/amd64": "b4n1net-windows-amd64.exe",
}

// ErrNoEngine means the platform is not bundled and no override was given.
var ErrNoEngine = errors.New(
	"b4n1-net engine not found for this platform; set B4N1NET_BIN_PATH",
)

// Binary resolves the engine path: the override wins, then the bundled copy.
func Binary() (string, error) {
	if override := os.Getenv("B4N1NET_BIN_PATH"); override != "" {
		if info, err := os.Stat(override); err == nil && !info.IsDir() {
			return override, nil
		}
		return "", ErrNoEngine
	}

	name, ok := binaries[runtime.GOOS+"/"+runtime.GOARCH]
	if !ok {
		return "", ErrNoEngine
	}
	// The module root is one level above this file's directory.
	root, err := moduleRoot()
	if err != nil {
		return "", err
	}
	bundled := filepath.Join(root, "bin", name)
	if info, err := os.Stat(bundled); err != nil || info.IsDir() {
		return "", ErrNoEngine
	}
	return bundled, nil
}

// moduleRoot walks up from the working directory until a bin/ with the engine
// exists, so the module works both from a checkout and from a vendored copy.
func moduleRoot() (string, error) {
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		if info, err := os.Stat(filepath.Join(dir, "bin")); err == nil && info.IsDir() {
			return dir, nil
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", ErrNoEngine
		}
		dir = parent
	}
}

// Client is a thin handle over the engine binary.
type Client struct {
	binary string
}

// New returns a client bound to the resolved engine.
func New() (*Client, error) {
	binary, err := Binary()
	if err != nil {
		return nil, err
	}
	return &Client{binary: binary}, nil
}

func (c *Client) text(args ...string) (string, error) {
	cmd := exec.Command(c.binary, args...)
	out, err := cmd.CombinedOutput()
	text := strings.TrimSpace(string(out))
	if err != nil {
		return text, err
	}
	return text, nil
}

// Version returns the engine version banner.
func (c *Client) Version() (string, error) { return c.text("--version") }

// Help returns the verb table.
func (c *Client) Help() (string, error) { return c.text("help") }

// Licenses prints the full license text; it never asks for a key.
func (c *Client) Licenses() (string, error) { return c.text("licenses") }

// Status reports the engine state; not running is a valid state.
func (c *Client) Status(json bool) (string, error) {
	return c.text(withJSON([]string{"status"}, json)...)
}

// Demo runs the offline demonstration (a real sealed loopback round trip).
func (c *Client) Demo(json bool) (string, error) {
	return c.text(withJSON([]string{"demo"}, json)...)
}

// Docs returns the bundled manual, optionally one section.
func (c *Client) Docs(section string) (string, error) {
	if section == "" {
		return c.text("docs")
	}
	return c.text("docs", "--section", section)
}

// Serve runs the receiving endpoint in the foreground.
func (c *Client) Serve(addr, secret string, json bool) (string, error) {
	args := []string{"serve", "--addr", addr}
	if secret != "" {
		args = append(args, "--secret", secret)
	}
	return c.text(withJSON(args, json)...)
}

// Send transmits one sealed frame to addr and waits for the acknowledgement.
func (c *Client) Send(addr, secret, message string, json bool) (string, error) {
	args := []string{"send", "--addr", addr}
	if secret != "" {
		args = append(args, "--secret", secret)
	}
	if message != "" {
		args = append(args, "--message", message)
	}
	return c.text(withJSON(args, json)...)
}

func withJSON(args []string, json bool) []string {
	if json {
		return append(args, "--json")
	}
	return args
}
