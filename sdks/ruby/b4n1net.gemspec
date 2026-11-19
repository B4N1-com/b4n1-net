# frozen_string_literal: true

require_relative "lib/b4n1net"

Gem::Specification.new do |spec|
  spec.name          = "b4n1net"
  spec.version       = B4n1Net::SDK_VERSION
  spec.authors       = ["Bani Montoya"]
  spec.summary       = "Sovereign transport: sealed UDP frames with HMAC, AEAD and acknowledgements."
  spec.homepage      = "https://b4n1.com"
  spec.license       = "BUSL-1.1"
  spec.required_ruby_version = ">= 3.0"

  spec.files = Dir["lib/**/*.rb", "bin/*", "README.md", "LICENSE", "EULA.txt"]
  spec.bindir = "bin"
  spec.require_paths = ["lib"]

  spec.metadata = {
    "source_code_uri" => "https://b4n1.com",
    "eula" => "EULA.txt"
  }
end
